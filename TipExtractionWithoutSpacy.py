# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 19:07:03 2017

@author: abc
"""

import nltk
from nltk.util import ngrams
from nltk import load
import nltk.data
import string
from bs4 import BeautifulSoup
import os
import pandas as pd

def getPOSterms(terms,POStags,tagger):
    tagged_terms=tagger.tag(terms)
    POSterms={}
    for tag in POStags:POSterms[tag]=set()
    for pair in tagged_terms:
        for tag in POStags: 
            if pair[1].startswith(tag):
                POSterms[tag].add(pair[0])
    return POSterms

def csvCreator(reviews,ext):
    t = [""] * len(reviews)
    for y in range(len(ext)):
        for z in range(len(reviews)):
            if reviews[z].find(ext[y]) != -1:
                t[z] = t[z] + " " + ext[y]
    panda = pd.DataFrame({'reviews':reviews, 'extracted':t})
    return(panda)

def printReview(sentence, tagger):
    #print(sentence)
    #sentence = "I've had chicken tacos, fish tacos, beef and chicken burritos, Frijoles and fajitas.. the spot is authentic."
    
    POStags=['NN','RB','VB','JJ','MD','PR']
    terms = nltk.word_tokenize(sentence.lower())
    #print(tagger.tag(terms))
    POSterms = getPOSterms(terms,POStags,tagger)
    nouns = POSterms['NN']
    adverbs = POSterms['RB']
    verbs = POSterms['VB']
    adjectives = POSterms['JJ']
    modalAuxilary = POSterms['MD']
    pronouns = POSterms['PR']
    #print(adverbs)
    #print(adjectives)
    #print(nouns)
    if(len(terms) > 3):
        fourgrams = ngrams(terms,4)
        for tg in fourgrams:
            case1 = tg[0] in nouns and tg[1] in verbs and tg[2] in adverbs and tg[3] in adjectives
            case2 = tg[0] in nouns and tg[1] in verbs and tg[2] in adjectives
            case3 = tg[0] in adverbs and tg[1] in adjectives and tg[2] in nouns
            case4 = tg[0] in nouns and tg[1] in verbs and tg[3] in adjectives
            case5 = tg[1] in nouns and tg[2] in verbs and tg[3] in adjectives
            case6 = tg[1] in adverbs and tg[2] in adjectives and tg[3] in nouns
            case7 = tg[0] in adjectives and tg[1] in adjectives and tg[2] in adjectives and tg[3] in nouns
            case8 = tg[0] in pronouns and tg[1] in modalAuxilary and tg[2] in verbs
            #case9 = tg[1] in adjectives and tg[2] in nouns and tg[3] in nouns
            case10 = tg[0] in pronouns and tg[1] in modalAuxilary and tg[3] in verbs
            case11 = tg[1] in verbs and tg[2] in adverbs and tg[3] in adjectives
            case12 = tg[1] in adjectives and tg[2] in adjectives and tg[3] in nouns
            #case13 = tg[1] in verbs and tg[2] in pronouns and tg[3] in nouns
            #case14 = tg[0] in verbs and tg[1] in pronouns and tg[3] in nouns
            #case15 = tg[0] in pronouns and tg[1] in verbs and tg[3] in nouns
            #case16 = tg[0] in pronouns and tg[1] in verbs and tg[3] in adjectives
            #print(tg)
            if(case1 or case2 or case3 or case4 or case5 or case6 or case7 or case8 or case10 or case11 or case12):
                #print(tg)
                #print('case1',case1,'case2',case2,'case3',case3,'case4',case4,'case5',case5,'case6',case6)
                #print('case7',case7,'case8',case8,'case10',case10,'case11',case11,'case12',case12)
                return(sentence)
            #if(case13 or case14 or case15 or case16):
                #print(tg)
                #print('case11',case11,'case12',case12,'case13',case13,'case14',case14)
#                return(sentence)
                
        
        sentence = sentence.translate(str.maketrans('','',string.punctuation))
        #specialCase1 recommend
        #print(sentence)
        for word in sentence.lower().strip().split(sep=' '):
            if word == 'recommend':
                return(sentence)
        #specialCase2 must or must've
        for word in sentence.lower().strip().split(sep=' '):
            if word == 'must' or word == "must've":
                return(sentence)
        #specialCase3 amazing
        for word in sentence.lower().strip().split(sep=' '):
            if word == 'amazing':
                return(sentence)
        #specialCase4 Dont miss or Do not miss
        notContains = sentence.find('Dont miss') == -1 and sentence.find('Do not miss') == -1
        if not notContains:
            return(sentence)
        #specialCase5 definitely
        for word in sentence.lower().strip().split(sep=' '):
            if word == 'definitely':
                return(sentence)
        #specialCase6 amazing
        for word in sentence.lower().strip().split(sep=' '):
            if word == 'delicious' or word == 'fantastic':
                return(sentence)
        #specialCase7 byob
        for word in sentence.lower().strip().split(sep=' '):
            if word == 'byob':
                return(sentence)
        #specialCase8 bland
        for word in sentence.lower().strip().split(sep=' '):
            if word == 'bland':
                return(sentence)
        #specialCase9 reservation
        for word in sentence.lower().strip().split(sep=' '):
            if word == 'reservation':
                return(sentence)
            
def htmlParser(path): # 17 sec  for 1416 reviews ~ 83 reviews/sec
    revlist= []
#    startTime= datetime.now() 
    for file in os.listdir(path):
        if file.endswith(".html"):
            with open(path +'/' +file, encoding= 'utf-8') as f:
                html = f.read()
            bs = BeautifulSoup(html, 'lxml')
            for node in bs.findAll('div', {'class':'review-content'}):
                for nod in node.findAll('p', {'lang':'en'}):
                    revlist.append(nod.text)
#    timeElapsed=datetime.now()-startTime 
#    print('Time elpased (hh:mm:ss.ms) {}'.format(timeElapsed))
    return(revlist)

if __name__ == '__main__':
    _POS_TAGGER = 'taggers/maxent_treebank_pos_tagger/english.pickle'
    tagger = load(_POS_TAGGER)
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    path = 'D:/Python/tipextractor' # forward slash always

### EXTRACT REVIEWS FROM HTML FILES
    reviews = htmlParser(path)
    rev = " ".join(reviews)
    rev = tokenizer.tokenize(rev)
###

### EXTRACT TIPS USING RULES    
    ext = []
#    startTime= datetime.now() 
    for x in rev:
        ext.append(printReview(x, tagger))
#    timeElapsed=datetime.now()-startTime 
#    print('Time elpased (hh:mm:ss.ms) {}'.format(timeElapsed))
    
    ext = [y for y in ext if y != None]

### CREATE A CSV OF REVIEWS AND THEIR TIPS EXTRACTED    
    panda = csvCreator(reviews,ext)
    panda = panda[['reviews', 'extracted']]
    panda.to_csv('D:/Python/tipextractor/ReviewsAndTips.csv', index =False)
