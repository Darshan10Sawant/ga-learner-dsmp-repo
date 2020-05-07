### Project Overview

 **Problem Statement**
You are given references to news pages collected from an web aggregator in the period from 10-March-2014 to 10-August-2014. The resources are grouped into categories that represent pages discussing the same story. News categories included in this dataset include business(b); science and technology(t); entertainment(e); and health(h).

The goal is to predict which class a particular resource belongs to given the title of the resource.

**__About the dataset__**
This dataset comes from the UCI Machine Learning Repository. In total there are 422937 resources available in the dataset. The columns included in this dataset are:

ID: the numeric ID of the article
TITLE: the headline of the article
URL: the URL of the article
PUBLISHER: the publisher of the article
CATEGORY: the category of the news item; one of: b:business, t:science and technology, e: entertainment and m:health
STORY: alphanumeric ID of the news story that the article discusses
HOSTNAME: hostname where the article was posted
TIMESTAMP: approximate timestamp of the article's publication, given in Unix time (seconds since midnight on Jan 1, 1970)


### Learnings from the project

 ### **_Why solve it_**
Solving it will reinforce the following concepts of text analytics:

Preprocess text data with tokenization, stopword removal etc
Vectorize data using Bag-of-words and TF-IDF approaches
Apply classifiers (Logistic and Multinomial Naive Bayes) to perform multi-class classification


### Approach taken to solve the problem

 i used count vectorizer and tfidf vectorizer on two different models:
        1)"MultinomialNB " on both vectorizers
        2)"OneVsRestClassifier(LogisticRegression) on both vectorizers


### Challenges faced

 1) Data preprocessing
2) i checked  catogories counts of target column , it was well balanced: e    152469   (entertainment)
                                                                                                                                b     115967 (business)
                                                                                                                                t        108344 (science and technology)
                                                                                                                                m     45639   (health)
                                                                                                                                Name: CATEGORY, dtype: int64
                                                                       


