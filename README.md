# #2024election: An Exploratory Analysis of Politicultural Communities on TikTok (Anticipated Completion, June 2026)

## University of Chicago Computational Social Science Master's Thesis

by Anita Sun

## Abstract:

This thesis explores how cultural discourse varies in both structure and content across political party lines on TikTok. To answer this question, I take presidential candidate accounts as partisan representations and examine the TikTok videos reposted by followers of candidate accounts. To analyze the TikTok repost data, I employ frequent itemset mining, social network analysis, and BERTopic modeling. I find that the semantic communities in Trump followers’ reposts are more overlapping and less distinct than those found in Harris followers’ reposts. I find that Harris followers’ reposts cover a wider breadth of topics. I analyze several emergent themes in the content of the reposts, finding connections to gender, sexuality, and violence. These findings corroborate current literature surrounding American partisanship, culture, and social media. I discuss how TikTok mediates and produces culture, indicating that future research is needed to understand the political relevance and impact of the social media platform.

## Background and Research Question:

TikTok has exploded in its popularity and relevance to the broader public, especially with younger generations. This repository is the culmination of a research design of an exploratory analysis of differences in behavior and interests by partisan affiliation on TikTok through the case study of the 2024 American Presidential election. The intended dataset takes on a treelike spanning structure, as demonstrated by this following figure:

![data structure image](/viz/Data_Structure.svg)

From official presidential campaign TikTok accounts, I will gather all of the public follower accounts who were following on or prior to Nov. 5, 2024. From this pool of followers, I will then collect their reposted TikTok videos and their following networks. This dataset will lend itself to NLP and sentiment analysis, as well as a social network analysis. This will allow me to explore the differences between liberal and conservative American users on TikTok.

## Repository Information


```

├── README.md: this file
├── annot_bib.bib: DELETE ME
├── association_rules.csv: CSV containing data of mined hashtag association rules
├── bertopic_crossfold.ipynb: Notebook containing code for BERTopic analysis. This notebook was initially hosted on Google CoLab for access to GPU compute resource.
├── k_betweenness.json: JSON file containing data of betweenness scores for nodes in the Harris co-occurrence hashtag network
├── k_degree.json: JSON file containing data of normalized degree scores for nodes in the Harris co-occurrence hashtag network
├── k_pagerank.json: JSON file containing data of pagerank scores for nodes in the Harris co-occurrence hashtag network
├── kamala_nodes_measure.csv: CSV file containing betweenness, degree, and pagerank scores of nodes in the Harris co-occurrence hashtag network. A consolidation of the data found in k_betweenness.json, k_degree.json, and k_pagerank.json
├── kamalahq_hashtag_network.edgelist: an edgelist file for the Harris co-occurrence hashtag network
├── kamalahq_hashtag_network.graphml: a GRAPHml file for the Harris co-occurrence hashtag network. DELETE ME
├── main.tex: a LaTex file with typesetting for the thesis draft(s)
├── network.ipynb: Notebook containing code for creating, analyzing, and visualizing co-occurrence hashtag networks
├── network_t_test.csv: CSV containing information for Table 2 (is labeled \ref{network_stat} in the main.tex)
├── references_test.bib: BIB file for all the references cited in the thesis
├── requirements.txt: DELETE ME (out of date)
├── scraping.py: Python script containing all the code used for scraping TikTok video data. Note: in order to run this script, it requires the user to obtain access to the TikTok Research Tools API
├── spark_itemset.ipynb: Notebook containing all the code used to mine and analyze frequent hashtag itemsets
├── t_betweenness.json: JSON file containing data of betweenness scores for nodes in the Trump co-occurrence hashtag network
├── t_degree.json: JSON file containing data of normalized degree scores for nodes in the Harris co-occurrence hashtag network
├── t_pagerank.json: JSON file containing data of pagerank scores for nodes in the Trump co-occurrence hashtag network
├── teamtrump_hashtag_network.edgelist: an edgelist file for the Trump co-occurrence hashtag network.
├── trump_nodes_measure.csv: CSV file containing betweenness, degree, and pagerank scores of nodes in the Trump co-occurrence hashtag network. A consolidation of the data found in t_betweenness.json, t_degree.json, and t_pagerank.json
└── viz: folder containing visualizations. Note: not all visualizations are included in main.tex
    ├── Data_Structure.svg
    ├── Data_Structure_Cohash.svg
    ├── Design_flow.png
    ├── Shield.png
    ├── avg_cosine_similarity_dist.png
    ├── bertopic_over_time.png
    ├── cofollowing_net.png
    ├── cohashtag_net.png
    ├── degree_density.png
    ├── descriptive_statistics_table.png
    ├── descriptive_statistics_table_all_tokens.png
    ├── document_visualization.png
    ├── emotion_topic_sankey.svg
    ├── great_table_itemset_stats.png
    ├── gt_association_rules.png
    ├── gt_kamala_association_rules.png
    ├── gt_kamala_association_rules_clean.png
    ├── gt_kamala_association_rules_lift.png
    ├── gt_network_stats.png
    ├── gt_trump_association_rules.png
    ├── gt_trump_association_rules_clean.png
    ├── gt_trump_association_rules_lift.png
    ├── hashtag_support.png
    ├── intertopic_distance.png
    ├── kamala_association_rules.png
    ├── kamala_association_rules_all_tokens.png
    ├── kamala_hierarchical_cluster.png
    ├── kamala_high_centrality.png
    ├── kamala_high_centrality_nohack.png
    ├── kamala_topic_matrix.png
    ├── kamala_topic_word_score.png
    ├── network_t_test.png
    ├── num_topics_dist.png
    ├── pretty_word_metrics.png
    ├── roberta_over_time.png
    ├── rule_confidence_dist.png
    ├── rule_lift_dist.png
    ├── rule_support_dist.png
    ├── silhouette_score_dist.png
    ├── singleton_support.png
    ├── topic_model_stat.png
    ├── topic_word_scores.png
    ├── trump_association_rules.png
    ├── trump_association_rules_all_tokens.png
    ├── trump_hierarchical_cluster.png
    ├── trump_high_centrality.png
    ├── trump_high_centrality_nohack.png
    ├── trump_topic_matrix.png
    └── trump_topic_word_score.png
```

## How to Cite

Sun, Anita (2026). _#2024election: An Exploratory Analysis of Politicultural Communities on TikTok_. https://github.com/nitomanto/the-t-word.
