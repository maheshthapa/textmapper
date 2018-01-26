# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 22:06:44 2018

@author: mahesh
"""


import textmapper as tm
import pprint
import json
import os
from gensim import corpora, models


# Generate topic model and topics 
## Read the serialized corpora file ##
corpus_dir = 'D:/giant/computer/thesis/textmapper/sample/earthquake_nepal/corpus_dir'
corpusfile = os.path.join(corpus_dir, 'eq.mm')
corpus = corpora.MmCorpus(corpusfile)

# Read dictionary
dictionaryfile = os.path.join(corpus_dir, 'eq.dict')
dictionary = corpora.Dictionary.load(dictionaryfile)


hdp = models.HdpModel(corpus,id2word=dictionary)