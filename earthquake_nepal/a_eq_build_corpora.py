# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 19:01:52 2018

@author: mahesh
"""

import textmapper as tm
import pprint
import json
import os
from gensim import corpora


import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# Creates and serializes corpus, dictionary and model

# Serialize corpus from documents 
#doc_dir = 'D:/textdata_20'
doc_dir = 'D:/giant/computer/thesis/textmapper/sample/earthquake_nepal/textdata'
corpus_dir = 'D:/giant/computer/thesis/textmapper/sample/earthquake_nepal/corpus_dir'
tm.serialize_corpus(doc_dir, corpus_dir)


# Generate topic model and topics 
## Read the serialized corpora file ##
corpus_dir = 'D:/giant/computer/thesis/textmapper/sample/earthquake_nepal/corpus_dir'
corpusfile = os.path.join(corpus_dir, 'corpus.mm')
corpus = corpora.MmCorpus(corpusfile)

# Read dictionary
dictionaryfile = os.path.join(corpus_dir, 'corpus.dict')
dictionary = corpora.Dictionary.load(dictionaryfile)

model ='lda' # Topic Modeling Algorithm
num_topics = 7 # Number of topics
topic_model = tm.extract_topic_model(corpus,dictionary, model, num_topics )
topic_model.save(os.path.join(corpus_dir,'topic_model.model'))



#write the topics into a file
f = open(os.path.join(os.path.dirname(corpus_dir),'map','data','topics.js'),'w+')
topics = topic_model.show_topics(num_topics = topic_model.num_topics, num_words = 10)
f.write("topics=" )
f.write(json.dumps(dict(topics)))
f.close()


pprint.pprint(topic_model.print_topics())





#tm.serialize_corpus(os.path.join(corpus_dir,corpus_name),corpus_dir) # Build and serialize corpus

#topic_model  = tm.extract_topic_model(corpus, 'lda', 2)
#topics = topic_model.print_topics()
##pprint.pprint('TOPICS: ',topic_model.print_topics())
#
## Convert to human redable form
#hrt = tm.convert_to_humanreadable(topics)
#print(hrt)


#hrt = [(0, ('nepal', 'earthquake', 'people', 'need', 'kathmandu', 'government', 'quake', 'area', 'help', 'day')), (1, ('nepal', 'earthquake', 'people', 'quake', 'country', 'kathmandu', 'damage', 'relief', 'government', 'disaster'))]
#
## Extract sentences
#folder = 'D:/giant/computer/thesis/topic_model/testdata/eq_sm/gp'
#topic = hrt[0]
#sent_list_of_lists = tm.extract_sentence_from_folder(folder,hrt[0])
#
## Geoparse
#geoobject = {
#  "type": "FeatureCollection",
#  "properties": {
#    "apiVersion": "0.5.1",
#    "source": "geoparser.io",
#    "id": "KbjJB4TX4Exu2oLJ8JaD"
#  },
#  "features": []
#}
#
#for item in sent_list_of_lists:
#    for i,sent in enumerate(item):
#        #features = (tm.geoparse_sentence(sent))["features"]
#        features_list = (json.loads(tm.geoparse_sentence(sent)))["features"]
#
#        for f in features_list:
#            geoobject["features"].append(f)
#
#print(json.dumps(geoobject))
#           








