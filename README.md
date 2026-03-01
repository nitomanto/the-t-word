# The T Word (In Progress, Anticipated Completion June 2026)

## University of Chicago Computational Social Science Master's Thesis

by Anita Sun

## Background and Research Question:

TikTok has exploded in its popularity and relevance to the broader public, especially with younger generations. This repository is the culmination of a research design of an exploratory analysis of differences in behavior and interests by partisan affiliation on TikTok through the case study of the 2024 American Presidential election. The intended dataset takes on a treelike spanning structure, as demonstrated by this following figure:

![data structure image](/viz/Data_Structure.svg)

From official presidential campaign TikTok accounts, I will gather all of the public follower accounts who were following on or prior to Nov. 5, 2024. From this pool of followers, I will then collect their reposted TikTok videos and their following networks. This dataset will lend itself to NLP and sentiment analysis, as well as a social network analysis. This will allow me to explore the differences between liberal and conservative American users on TikTok.

## Repository Information


```

├── MACS 30200 Final Presentation.pdf: PDF slide deck for proposal presentation
├── README.md: this file
├── annot_bib.bib: Annotated preliminary bibliography for literature review
├── references.bib: Updated, expanded bibliogrpahy for literature review and other references
├── main.tex: Main document consisting of full proposal
├── mockup_data.ipynb: Notebook containing code for generating mockup visualizations
├── mockup_data.tex: .tex file containing code for a rough draft of a Results section
├── requirements.txt: .txt file containing information for packages and versioning
├── roberta_bertopic_merged.csv: csv file containing data for mockup_data.ipynb
├── viz: folder for saved visualizations
│   ├── Data_Structure.svg: the image describing the structure of the dataset
│   ├── bertopic_over_time.png: visual showing Trump's Tweet BERTopic frequencies over time
│   ├── cofollowing_net.png: example visualization of constructed network
│   ├── cohashtag_net.png: example visualization of constructed network
│   ├── emotion_topic_sankey.svg: visual showing Trump's Tweet BERTopic distribution across RoBERTa emotions
│   ├── intertopic_distance.png: example visualization of BERTopic clusters after dimension reduction
│   ├── pretty_word_metrics.png: example table of a textual network analysis
│   ├── topic_word_scores.png: example table displaying tf-idf scores for BERTopic clusters
│   └── roberta_over_time.png: visual showing Trump's Tweet RoBERTa emotion frequencies over time
└── words_dat.txt.gz: .txt file used to generate mockups in mockup_data.ipynb
```

## How to Cite

Sun, Anita (2025). _#2024election: An Exploratory Analysis of Partisan Entertainment on TikTok_. https://github.com/macs30200-s23/course-project-nitomanto
