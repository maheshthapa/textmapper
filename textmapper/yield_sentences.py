# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 23:24:52 2018

@author: mahesh
"""
import spacy
import os

nlp = spacy.load('en')


def extract_sentence_from_file(file, topic):
    """
    Extracts generator of sentences if the sentence contains one of the terms..
    ..of the topics. 
    """
    file = open(file).read()
    doc = nlp(file)
    sent_list = []
    for sent in doc.sents:
        tokens = set([token.lemma_ for token in sent])
        if tokens.intersection(topic[1]):
            sent_list.append(sent.text)
    return sent_list
            
        
    
def extract_sentence_from_folder(folder,topic):
    sent_list_of_lists = []
    for root, dirs, files in os.walk(folder):
        for fname in filter(lambda fname: fname.endswith('.txt'), files):
            file_name = os.path.join(root, fname)
            
            sent_list = extract_sentence_from_file(file = file_name, topic = topic)
            if sent_list:
                sent_list_of_lists.append(sent_list)
    return sent_list_of_lists


if __name__ == '__main__':
    file = 'D:/giant/computer/thesis/topic_model/testdata/eq_sm/eq_data/bbc _2015_5_12.txt'
    folder = 'D:/giant/computer/thesis/topic_model/testdata/eq_sm/eq_data'
    topic = (0,  ('nepal',
   'earthquake',
   'people',
   'kathmandu',
   'quake',
   'day',
   'village',
   'government',
   'house',
   'country'))
    
#    sent_with_topic = (yield_sentence_from_file(file,topic))
#    print(sent_with_topic)
   
    sent_list_of_lists = (extract_sentence_from_folder(folder,topic))
    print(sent_list_of_lists)
   

    #y = yield_sentence_from_file()
