# =======================================================================================================
# Table of Contents START
# =======================================================================================================

'''
1. Orientation
2. Imports
3. get_blog_articles
4. get_news_articles
5. function3
6. function4
7. function5
'''

# =======================================================================================================
# Table of Contents END
# Table of Contents TO Orientation
# Orientation START
# =======================================================================================================

'''
The purpose of this file is to create functions specifically for the 'acquire.ipynb'
file and anything else that may be of use.
'''

# =======================================================================================================
# Orientation END
# Orientation TO Imports
# Imports START
# =======================================================================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from bs4 import BeautifulSoup
from requests import get
import os
import env

# =======================================================================================================
# Imports END
# Imports TO get_blog_articles
# get_blog_articles START
# =======================================================================================================

def get_blog_articles():
    '''
    Gets the title and contents of each blog article from the codeup blog
    site https://codeup.com/blog/
    
    INPUT:
    NONE
    
    OUTPUT:
    blogs_dict = Dictionary of all pertinent information
    '''
    url = 'https://codeup.com/blog/'
    headers = {'User-Agent' : 'Codeup Data Science'}
    response = get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    valid_articles = []
    unchecked_articles = soup.find_all('h2')
    for article in unchecked_articles:
        if article.a != None:
            valid_articles.append(article)
    titles = []
    valid_content_url = []
    orientation_content = []
    paragraph_one_content = []
    paragraph_two_content = []
    paragraph_three_content = []
    for article in valid_articles:
        titles.append(article.a.text)
        contenturl = article.a['href']
        headers = {'User-Agent' : 'Codeup Data Science'}
        response = get(contenturl, headers=headers)
        if response.status_code == 200:
            valid_content_url.append(contenturl)
            content_soup = BeautifulSoup(response.content, 'html.parser')
            divs = content_soup.find_all('div', class_='entry-content')
            for div in divs:
                    paragraphs = div.find_all('p')
                    orientation_paragraph = paragraphs[0].text
                    first_content_paragraph = paragraphs[3].text
                    second_content_paragraph = paragraphs[4].text
                    try:
                        third_content_paragraph = paragraphs[5].text
                    except IndexError:
                        third_content_paragraph = ('None')
                    orientation_content.append(orientation_paragraph)
                    paragraph_one_content.append(first_content_paragraph)
                    paragraph_two_content.append(second_content_paragraph)
                    paragraph_three_content.append(third_content_paragraph)
    blogs_dict = {
        'article_title' : titles,
        'article_url' : valid_content_url,
        'article_orientation' : orientation_content,
        'article_first_paragraph' : paragraph_one_content,
        'article_second_paragraph' : paragraph_two_content,
        'article_third_paragraph' : paragraph_three_content
        }
    return blogs_dict
    
# =======================================================================================================
# get_blog_articles END
# get_blog_articles TO get_news_articles
# get_news_articles START
# =======================================================================================================

def get_news_articles():
    '''
    Gets the headline, summary, and category of each blog article from the inshorts
    site https://inshorts.com/
    
    INPUT:
    NONE
    
    OUTPUT:
    news_dict = Dictionary of all pertinent information
    '''
    headline_content = []
    summary_content = []
    category_content = []
    urls = [
        'https://inshorts.com/en/read/business',
        'https://inshorts.com/en/read/sports',
        'https://inshorts.com/en/read/technology',
        'https://inshorts.com/en/read/entertainment'
    ]
    url = urls[0]
    response = get(url)
    contents = BeautifulSoup(response.content, 'html.parser')
    articles = contents.find_all('div', class_='card-stack')
    for article in articles:
        headlines = article.find_all('span', itemprop='headline')
        summarys = article.find_all('div', itemprop='articleBody')
        for headline in headlines:
            headline_content.append(headline.text)
        for summary in summarys:
            summary_content.append(summary.text)
            category_content.append('Business')
    url = urls[1]
    response = get(url)
    contents = BeautifulSoup(response.content, 'html.parser')
    articles = contents.find_all('div', class_='card-stack')
    for article in articles:
        headlines = article.find_all('span', itemprop='headline')
        summarys = article.find_all('div', itemprop='articleBody')
        for headline in headlines:
            headline_content.append(headline.text)
        for summary in summarys:
            summary_content.append(summary.text)
            category_content.append('Sports')
    url = urls[2]
    response = get(url)
    contents = BeautifulSoup(response.content, 'html.parser')
    articles = contents.find_all('div', class_='card-stack')
    for article in articles:
        headlines = article.find_all('span', itemprop='headline')
        summarys = article.find_all('div', itemprop='articleBody')
        for headline in headlines:
            headline_content.append(headline.text)
        for summary in summarys:
            summary_content.append(summary.text)
            category_content.append('Technology')
    url = urls[3]
    response = get(url)
    contents = BeautifulSoup(response.content, 'html.parser')
    articles = contents.find_all('div', class_='card-stack')
    for article in articles:
        headlines = article.find_all('span', itemprop='headline')
        summarys = article.find_all('div', itemprop='articleBody')
        for headline in headlines:
            headline_content.append(headline.text)
        for summary in summarys:
            summary_content.append(summary.text)
            category_content.append('Entertainment')
    news_dict = {
        'category' : category_content,
        'headline' : headline_content,
        'summary' : summary_content
        }
    return news_dict
    
# =======================================================================================================
# get_news_articles END
# get_news_articles TO function3
# function3 START
# =======================================================================================================


    
# =======================================================================================================
# function3 END
# function3 TO function4
# function4 START
# =======================================================================================================


    
# =======================================================================================================
# function4 END
# function4 TO function5
# function5 START
# =======================================================================================================