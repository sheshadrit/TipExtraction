import nltk
from nltk.util import ngrams
from nltk import load
import nltk.data
import string
import pandas as pd
from pattern.en import mood, Sentence
import spacy
import numpy as np
import os
os.chdir('D:/Python/tipextractor/')
from TipExtractor import printReview, getPOSterms

#from bs4 import BeautifulSoup
#from datetime import datetime 
#from sentence_sem_sim import sen_sem_sim    
#from sklearn.metrics.pairwise import cosine_similarity
#from sklearn.feature_extraction.text import TfidfVectorizer


if __name__ == "__main__":
    df = pd.read_csv("D:\\Python\\tipextractor\\manualscrape\\ital100.csv")
    df = df.append(pd.read_csv("D:\\Python\\tipextractor\\manualscrape\\tallascrappedall.csv"),ignore_index =True)
    df = df.append(pd.read_csv("D:\\Python\\tipextractor\\manualscrape\\mukulscrappedall.csv", encoding = 'latin-1'),ignore_index =True)
    df = df.append(pd.read_csv("D:\\Python\\tipextractor\\manualscrape\\priyalscrappedall.csv", encoding = 'latin-1'),ignore_index =True)


    nlp = spacy.load('en')
    _POS_TAGGER = 'taggers/maxent_treebank_pos_tagger/english.pickle'
    tagger = load(_POS_TAGGER)
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

    reviews = df['title'].tolist()
    rev = " ".join(reviews)
    rev = tokenizer.tokenize(rev)
    
    tip = df['tip'].tolist()
    tip = " ".join(tip)
    tip = tokenizer.tokenize(tip)

    ext = []
    for x in rev:
        ext.append(printReview(x, tagger,nlp))
    
    ext = [y for y in ext if y != None]
    
    print(len(ext)/len(rev))
    
'''
    4259/7148 # ~ 60% of all sentences in all reviews are tips
    4259/1204 # detected vs manual detected 
'''    
    ext = []
    for x in tip:
        ext.append(printReview(x, tagger,nlp))
    
    ext = [y for y in ext if y != None]
    
    print('Accuracy: {}'.format(len(ext)/len(tip)))

'''  
    846/1204 # ~ 70% Accuracy
'''

