# =======================================================================================================
# Table of Contents START
# =======================================================================================================

'''
1. Orientation
2. Imports
3. basic_clean
4. tokenize
5. stem
6. lemmatize
7. remove_stopwords
8. full_clean
9. prepare_blog_articles
10. prepare_news_articles
11. all_versions_clean
12. all_versions_news
'''

# =======================================================================================================
# Table of Contents END
# Table of Contents TO Orientation
# Orientation START
# =======================================================================================================

'''
The purpose of this file is to create functions specifically for the 'prepare.ipynb'
file and anything else that may be of use.
'''

# =======================================================================================================
# Orientation END
# Orientation TO Imports
# Imports START
# =======================================================================================================

import numpy as np
import pandas as pd
import re
import nltk
import unicodedata
import acquire as a
import prepare as p
import os

# =======================================================================================================
# Imports END
# Imports TO basic_clean
# basic_clean START
# =======================================================================================================

def basic_clean(entry):
    '''
    Takes in a pandas series (column), lowercases everything, normalizes unicode characters,
    and replaces anything that is not a letter, number, whitespace or a
    single quote
    
    INPUT:
    entry = Pandas series (column) that needs to be cleaned
    
    OUTPUT:
    cleaned = Pandas series (column) that is cleaned (I HAVE EXORCISED THE DEMON)
    '''
    removed_special = [re.sub(r'[^\w\s]', '', text) for text in entry]
    normalized = [unicodedata.normalize('NFKD',text).encode('ascii', 'ignore').decode('utf-8') for text in removed_special]
    lowered = [text.lower() for text in normalized]
    cleaned = lowered
    return cleaned
    
# =======================================================================================================
# basic_clean END
# basic_clean TO tokenize
# tokenize START
# =======================================================================================================

def tokenize(entry):
    '''
    Takes in a cleaned pandas series (column) and tokenizes all the words in the string
    
    INPUT:
    entry = Cleaned pandas series (Column) that needs to be tokenized
    
    OUTPUT:
    tokenized_data = Pandas series (Column) that is tokenized (I HAVE EXORCISED THE DEMON)
    '''
    tokenizer = nltk.tokenize.toktok.ToktokTokenizer()
    tokenized_data = [tokenizer.tokenize(text, return_str=True) for text in entry]
    return tokenized_data
    
# =======================================================================================================
# tokenize END
# tokenize TO stem
# stem START
# =======================================================================================================

def stem(entry):
    '''
    Takes in a cleaned and tokenized pandas series (column) and applies stemming to all the words
    
    INPUT:
    entry = Cleaned and tokenized pandas series (column) that needs to be stemmed
    
    OUTPUT:
    stemmed_data = Pandas series (column) that is stemmed (I HAVE EXORCISED THE DEMON)
    '''
    stemmer = nltk.porter.PorterStemmer()
    stemmed_data = []
    for text in entry:
        stemmed_tokens = [stemmer.stem(token) for token in text.split()]
        stemmed_text = ' '.join(stemmed_tokens)
        stemmed_data.append(stemmed_text)
    return stemmed_data
    
# =======================================================================================================
# stem END
# stem TO lemmatize
# lemmatize START
# =======================================================================================================

def lemmatize(entry):
    '''
    Takes in a cleaned and tokenized pandas series (column) and applies lemmatization to each word
    
    INPUT:
    entry = Cleaned and tokenized pandas series (column) that needs to be lemmatized
    
    OUTPUT:
    lemmatized_data = Pandas series (column) that is lemmatized (I HAVE EXORCISED THE DEMON)
    '''
    lemmatizer = nltk.stem.WordNetLemmatizer()
    lemmatized_data = []
    for text in entry:
        lemmatized_tokens = [lemmatizer.lemmatize(word) for word in text.split()]
        lemmatized_text = ' '.join(lemmatized_tokens)
        lemmatized_data.append(lemmatized_text)
    return lemmatized_data
    
# =======================================================================================================
# lemmatize END
# lemmatize TO remove_stopwords
# remove_stopwords START
# =======================================================================================================

def remove_stopwords(entry, extra_words=[], exclude_words=[]):
    '''
    Takes in a cleaned, tokenized, and stemmed/lemmatized pandas series (column) and removes all of the stopwords
    
    INPUT:
    entry = Cleaned, tokenized, and stemmed/lemmatized pandas series (column) that needs stopwords removed
    extra_words = Additional words to include for removal
    exclude_words = Words to exclude from removal
    
    OUTPUT:
    removed_stopwords = Pandas series (column) that has stopwords removed (I HAVE EXORCISED THE DEMON)
    '''
    stopwords = nltk.corpus.stopwords
    removed_stopwords = []
    for text in entry:
        not_stopword = [word for word in text.split() if word not in stopwords.words('english') or word in extra_words and word not in exclude_words]
        no_stopwords = ' '.join(not_stopword)
        removed_stopwords.append(no_stopwords)
    return removed_stopwords

# =======================================================================================================
# remove_stopwords END
# remove_stopwords TO full_clean
# full_clean START
# =======================================================================================================

def full_clean(entry, stem_method=False, extra_words=[], exclude_words=[]):
    '''
    Takes in a pandas series (column) and conducts the basic_clean, tokenize, stem/lemmatize
    (Lemmatize by default), and the remove_stopwords functions all at once rather than having to run the functions separately
    
    INPUT:
    entry = Pandas series (column) that needs to be cleaned from start to finish
    stem_method = Boolean True/False: False for stemming and True for lemmatizing
    extra_words = Additional words to include for removal
    exclude_words = Words to exclude from removal
    
    OUTPUT:
    full_cleaned_data = Pandas series (column) that has stopwords removed (I HAVE EXORCISED THE DEMON)
    '''
    cleaned = basic_clean(entry)
    tokenized = tokenize(cleaned)
    if stem_method == True:
        stemmed_or_lemmatized = stem(tokenized)
    else:
        stemmed_or_lemmatized = lemmatize(tokenized)
    removed_stopwords = remove_stopwords(stemmed_or_lemmatized, extra_words=extra_words, exclude_words=exclude_words)
    full_cleaned_data = removed_stopwords
    return full_cleaned_data

# =======================================================================================================
# full_clean END
# full_clean TO prepare_blog_articles
# prepare_blog_articles START
# =======================================================================================================

def prepare_blog_articles():
    '''
    Acquires the vanilla blog articles dataframe via web scraping then prepares
    pertinent columns and returns the prepared dataframe for exploration
    
    INPUT:
    NONE
    
    OUTPUT:
    prepared_blog_articles = Pandas dataframe of prepared blog article data
    '''
    codeup_df = a.get_blog_articles()
    codeup_df['article_orientation'] = codeup_df.article_orientation.fillna('None')
    codeup_df['article_orientation'] = p.full_clean(codeup_df.article_orientation)
    codeup_df['article_first_paragraph'] = p.full_clean(codeup_df.article_first_paragraph)
    codeup_df['article_second_paragraph'] = p.full_clean(codeup_df.article_second_paragraph)
    codeup_df['article_third_paragraph'] = p.full_clean(codeup_df.article_third_paragraph)
    prepared_blog_articles = codeup_df
    return prepared_blog_articles

# =======================================================================================================
# prepare_blog_articles END
# prepare_blog_articles TO prepare_news_articles
# prepare_news_articles START
# =======================================================================================================

def prepare_news_articles():
    '''
    Acquires the vanilla news articles dataframe via web scraping then prepares
    pertinent columns and returns the prepared dataframe for exploration
    
    INPUT:
    NONE
    
    OUTPUT:
    prepared_news_articles = Pandas dataframe of prepared news article data
    '''
    news_articles = a.get_news_articles()
    news_articles['headline_clean'] = p.full_clean(news_articles.headline)
    news_articles['summary_clean'] = p.full_clean(news_articles.summary)
    prepared_news_articles = news_articles
    return prepared_news_articles

# =======================================================================================================
# prepare_news_articles END
# prepare_news_articles TO all_versions_clean
# all_versions_clean START
# =======================================================================================================

def all_versions_blog():
    '''
    Acquires the vanilla blog articles dataframe via web scraping then prepares
    pertinent columns and returns the prepared dataframe with all versions of cleaning for exploration
    
    INPUT:
    NONE
    
    OUTPUT:
    all_versions_blog_df = Pandas dataframe of all prepared versions blog article data
    '''
    codeup_df = a.get_blog_articles()
    columns_to_adjust = [
        'article_orientation',
        'article_first_paragraph',
        'article_second_paragraph',
        'article_third_paragraph'
    ]
    codeup_df['article_orientation'] = codeup_df.article_orientation.fillna('None')
    for col in columns_to_adjust:
        codeup_df.rename(columns={col : f'{col}_original'}, inplace=True)
        clean = p.basic_clean(codeup_df[f'{col}_original'])
        clean = p.tokenize(clean)
        clean = p.remove_stopwords(clean)
        stemmed = p.stem(clean)
        lemmatized = p.lemmatize(clean)
        codeup_df[f'{col}_cleaned'] = clean
        codeup_df[f'{col}_stemmed'] = stemmed
        codeup_df[f'{col}_lemmatized'] = lemmatized
    all_versions_blog_df = codeup_df
    return all_versions_blog_df


# =======================================================================================================
# all_versions_clean END
# all_versions_clean TO all_versions_news
# all_versions_news START
# =======================================================================================================

def all_versions_news():
    '''
    Acquires the vanilla news articles dataframe via web scraping then prepares
    pertinent columns and returns the prepared dataframe with all versions of cleaning for exploration
    
    INPUT:
    NONE
    
    OUTPUT:
    all_versions_news_df = Pandas dataframe of all prepared versions news article data
    '''
    news_df = a.get_news_articles()
    columns_to_adjust = [
        'headline',
        'summary'
    ]
    for col in columns_to_adjust:
        news_df.rename(columns={col : f'{col}_original'}, inplace=True)
        clean = p.basic_clean(news_df[f'{col}_original'])
        clean = p.tokenize(clean)
        clean = p.remove_stopwords(clean)
        stemmed = p.stem(clean)
        lemmatized = p.lemmatize(clean)
        news_df[f'{col}_cleaned'] = clean
        news_df[f'{col}_stemmed'] = stemmed
        news_df[f'{col}_lemmatized'] = lemmatized
    all_versions_news_df = news_df
    return all_versions_news_df

# =======================================================================================================
# all_versions_news END
# =======================================================================================================