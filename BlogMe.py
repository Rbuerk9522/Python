# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 23:21:56 2022

@author: Lenovo
"""

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# Reading the xlsx File
Articles = pd.read_excel('articles.xlsx')

#Exploring the data
Articles.describe()

Articles.info()

#Counting articles per source
source_count = Articles.groupby(['source_id'])['article_id'].count()

#number of reactions by publisher
source_reaction = Articles.groupby(['source_id'])['engagement_reaction_count'].sum()

#Dropping unnecessary columns
Articles = Articles.drop('engagement_comment_plugin_count' , axis = 1)

#keyword flagging function
def keyword_search(keyword):
    length = len(Articles)
    keyword_flag = []
    for x in range(0, length): # for loop to isolate the rows
        heading = Articles['title'][x]
        try:
            if keyword in heading: # checking if keyword is in my heading
                flag = 1
            else:
                flag = 0
        except:
            flag = 0
        keyword_flag.append(flag)
    return keyword_flag

KeywordFlag = keyword_search('murder')

Articles['Keyword'] = KeywordFlag    


# SentimentIntensityAnalyzer

Sent_Int = SentimentIntensityAnalyzer()

text = Articles['title'][16]

sent = Sent_Int.polarity_scores(text)

neg = sent['neg']
pos = sent['pos']
neu = sent['neu']

title_neg_sentiment = []
title_pos_sentiment = []
title_neu_sentiment = []

length = len(Articles)

for x in range(0, length):
    try:
        text = Articles['title'][x]
        Sent_Int = SentimentIntensityAnalyzer()
        sent = Sent_Int.polarity_scores(text)
        neg = sent['neg']
        pos = sent['pos']
        neu = sent['neu']
    except:
        neg = 0
        pos = 0
        neu = 0
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)

title_neg_sentiment = pd.Series(title_neg_sentiment)
title_pos_sentiment = pd.Series(title_pos_sentiment)
title_neu_sentiment = pd.Series(title_neu_sentiment)

Articles['title_neg_sentiment'] = title_neg_sentiment
Articles['title_pos_sentiment'] = title_pos_sentiment
Articles['title_neu_sentiment'] = title_neu_sentiment

# Writing the data to an xlsx file
Articles.to_excel('blogme_clean.xlsx', sheet_name = 'blogmedata', index = False)





