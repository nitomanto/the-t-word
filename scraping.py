import sqlite3
import requests
import time
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
ACCESS_TOKEN = os.getenv("API_ACCESS_TOKEN")
HEADERS = {"Authorization": f"Bearer {ACCESS_TOKEN}", "Content-Type": "application/json"}
START_TS = int(datetime(2024, 7, 21).timestamp())
END_TS = int(datetime(2024, 11, 5).timestamp())
# IMPORTANT: for replication, replace "kamalahq" to most current account name ("headquarters")
TARGET_USERS = ["kamalahq", "teamtrump"]

def init_db():
    conn = sqlite3.connect('tiktok_breadth_first.db')
    cursor = conn.cursor()
    # User table with status flags for BFS tracking
    cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                      (username TEXT PRIMARY KEY, 
                       display_name TEXT, 
                       following_fetched INTEGER DEFAULT 0, 
                       reposts_fetched INTEGER DEFAULT 0)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS follow_relations 
                      (from_username TEXT, to_username TEXT, UNIQUE(from_username, to_username))''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS videos 
                      (reposter_username TEXT, id TEXT, create_time INTEGER, 
                       creator_username TEXT, video_description TEXT, hashtag_names TEXT, 
                       like_count INTEGER, comment_count INTEGER, view_count INTEGER, 
                       favorites_count INTEGER, PRIMARY KEY (reposter_username, id))''')
    conn.commit()
    return conn


def api_request(url, payload, fields=None):
    endpoint = url + (f"?fields={fields}" if fields else "")
    while True:
        response = requests.post(endpoint, headers=HEADERS, json=payload)
        if response.status_code == 200:
            return response.json().get('data', {})
        elif response.status_code == 429:
            print("Rate limit reached. Wait until limit resets.")
            return None
        else:
            print(f"Error {response.status_code}: {response.text}")
            return None


def phase_1_collect_followers(db, targets):
    """Collects all followers of target users first (The 'Seed' level)."""
    cursor = db.cursor()
    url = "https://open.tiktokapis.com/v2/research/user/followers/"
    for target in targets:
        print(f"Crawl Phase 1: Fetching all followers for @{target}")
        api_cursor = None
        has_more = True
        while has_more:
            payload = {"username": target, "max_count": 100}
            if api_cursor: payload["cursor"] = api_cursor
            data = api_request(url, payload)
            if not data: break
            
            for f in data.get('user_followers', []):
                cursor.execute("INSERT OR IGNORE INTO users (username, display_name) VALUES (?, ?)", 
                               (f['username'], f.get('display_name', '')))
                cursor.execute("INSERT OR IGNORE INTO follow_relations VALUES (?, ?)", 
                               (f['username'], target))
            
            api_cursor = data.get('cursor')
            has_more = data.get('has_more', False)
            db.commit()
        print(f"all followers fetched for @{target}")


def phase_2_fetch_following(db):
    """Refers back to DB to process following lists for collected users."""
    cursor = db.cursor()
    # Select users where we haven't fetched their following list yet
    query = """
    SELECT username
    FROM users
    JOIN follow_relations as fr
    ON fr.from_username = users.username
    WHERE users.following_fetched = 0
    AND (fr.to_username = 'teamtrump' OR fr.to_username = 'kamalahq')
    """
    cursor.execute(query)
    pending = cursor.fetchall()
    
    url = "https://open.tiktokapis.com/v2/research/user/following/"
    for (username,) in pending:
        print(f"Crawl Phase 2: Fetching following list for @{username}")
        data = api_request(url, {"username": username, "max_count": 100})
        if data:
            for followed in data.get('user_following', []):
                cursor.execute("INSERT OR IGNORE INTO users (username) VALUES (?)", (followed['username'],))
                cursor.execute("INSERT OR IGNORE INTO follow_relations VALUES (?, ?)", (username, followed['username']))
            # Mark as done
            cursor.execute("UPDATE users SET following_fetched = 1 WHERE username = ?", (username,))
            db.commit()


def phase_3_fetch_reposts(db):
    """Refers back to DB to process reposts for collected users."""
    cursor = db.cursor()
    query = """ 
    SELECT username
    FROM users
    JOIN follow_relations as fr
    ON fr.from_username = users.username
    WHERE users.reposts_fetched = 0
    AND (fr.to_username = 'teamtrump' OR fr.to_username = 'kamalahq')
    ORDER BY RANDOM()
    LIMIT 1000
    """
    cursor.execute(query)
    pending = cursor.fetchall()
    
    url = "https://open.tiktokapis.com/v2/research/user/reposted_videos/"
    fields = "id,create_time,username,video_description,hashtag_names,like_count,comment_count,view_count"
    
    for (username,) in pending:
        print(f"Crawl Phase 3: Fetching reposts for @{username}")
        api_cursor = 0
        has_more = True
        while has_more:
            data = api_request(url, {"username": username, "max_count": 100, "cursor": api_cursor}, fields=fields)
            if not data: 
                print("no data found, breaking")
                print(data)
                print("test")
                break
            
            for v in data.get('reposted_videos', []):
                cursor.execute("INSERT OR IGNORE INTO videos VALUES (?,?,?,?,?,?,?,?,?,?)", 
                    (username, v['id'], v['create_time'], v['username'], 
                     v.get('video_description', ''), ",".join(v.get('hashtag_names', [])),
                     v.get('like_count', 0), v.get('comment_count', 0), 
                     v.get('view_count', 0), v.get('favourites_count', 0)))
            
            api_cursor = data.get('cursor')
            has_more = data.get('has_more', False)
        
        cursor.execute("UPDATE users SET reposts_fetched = 1 WHERE username = ?", (username,))
        db.commit()


if __name__ == "__main__":
    db_conn = init_db()
    
    try:
        # Step 1: Ensure all primary followers are in the DB
        phase_1_collect_followers(db_conn, TARGET_USERS)
        
        # Step 2: Process their following relationships
        phase_2_fetch_following(db_conn)
        
        # Step 3: Process their reposted video history
        phase_3_fetch_reposts(db_conn)
        
    except KeyboardInterrupt:
        print("\nStopping... Progress has been saved to the database.")
    finally:
        db_conn.close()