# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 22:18:07 2017

@author: mahesh
"""

# import the necessary modules
import matplotlib.pyplot as plt
import gensim
import numpy as np
import spacy
import os
import pprint
import re

from gensim.models import CoherenceModel, LdaModel, LsiModel, HdpModel
from gensim.models.wrappers import LdaMallet
from gensim.corpora import Dictionary
from gensim.models import Phrases
from gensim.models.phrases import Phraser
from gensim import corpora

#import gensim.pyLDAvis

from IPython import get_ipython


import   warnings
warnings.filterwarnings('ignore')  # Let's not pay heed to them right now
get_ipython().run_line_magic('matplotlib', 'inline')


from spacy.tokens import Token
from spacy.lang.en.stop_words import STOP_WORDS  # import stop words from language data

stop_words_getter = lambda token: token.is_stop or token.lower_ in STOP_WORDS or token.lemma_ in STOP_WORDS
Token.set_extension('is_stop', getter=stop_words_getter)  # set attribute with getter



def build_corpus(doc_dir):
    """
    Extract topics given a folder location with one or more documents
    """
    #bigram = iter_bigram(document_loc)            
    corpus = TxtSubdirsCorpus(doc_dir) # create corpus
    
    return corpus
   
   
def serialize_corpus(doc_dir, corpus_dir):
    corpus_name = 'corpus.mm'
    dict_name = 'corpus.dict'
    corpus = build_corpus(doc_dir)

    corpora.MmCorpus.serialize(os.path.join(corpus_dir,corpus_name),corpus)
    
    corpus.dictionary.save(os.path.join(corpus_dir,dict_name))
    
    


def extract_topic_model(corpus, dictionary, model, num_topics):
    if model == 'lsi':
        lsimodel = LsiModel(corpus=corpus, num_topics=num_topics, id2word=dictionary)
        return lsimodel
    
    elif model == 'lda':
        ldamodel = LdaModel(corpus = corpus, id2word=dictionary, num_topics= num_topics)
        return ldamodel
    
    elif model == 'hdp':
        hdpmodel = HdpModel(corpus=corpus, id2word=dictionary)
        return hdpmodel
    

def iter_bigram(top_directory):
    """
    Iterate over all the documents to train the bigram
    """
    
    #nlp = spacy.load("en")
    #sentences = []
    #bigram = gensim.models.Phrases(min_count = 1, threshold =2 )
    
    #bigram = Phrases(min_count=1, threshold=2)
    bigram = gensim.models.Phrases( min_count = 20, threshold =10)
        
    # find all .txt documents, no matter how deep under top_directory
    for root, dirs, files in os.walk(top_directory):
        for fname in filter(lambda fname: fname.endswith('.txt'), files):
            # read each document as one big string
            document = open(os.path.join(root, fname)).read()
            
            tokens = gensim.utils.tokenize(document, lower=True, errors='ignore')
            
            #for i in tokens:
            #    token_list.append(i)
                       
            #print(token_list)
            #bigram = gensim.models.Phrases(token_list)
            
            #bigram_learn = bigram.learn_vocab(document.split())
            #print(document.split())
            #bigram.learn_vocab(document.split(),200)
            
            bigram.add_vocab(tokens)
            print([w for w in bigram.vocab])
#            for key in bigram.vocab.keys():
#                print(key)
#            
            #print(c)
            #print(dir(bigram))
            #bigram.add_vocab(token_list)
    #sent = [u'the', u'mayor', u'of', u'new', u'york', u'was', u'there']        
    return bigram            


def iter_documents(top_directory):
    """
    Generator: iterate over all relevant documents, yielding one
    document (=list of utf8 tokens) at a time.
    """
    #Spacy pipeline
    nlp = spacy.load('en')
    
    
    # STOP WORDS
    custom_stop_words = 'The I We But It say ’s A An \'s'.split()
    
    for word in custom_stop_words:
        lex = nlp.vocab[word]
        lex.is_stop = True
     
    # find all .txt documents, no matter how deep under top_directory
    for root, dirs, files in os.walk(top_directory):
        for fname in filter(lambda fname: fname.endswith('.txt'), files):
            # read each document as one big string
            document = open(os.path.join(root, fname)).read()
            
            # Create a doc object                        
            doc = nlp(document)
          
            # Tokenize and remove punctuation, space and stop words
            text = [token.lemma_ for token in doc if not token.is_punct and not token._.is_stop 
                    and token.text != '\n' and not token.like_num
                    and token.text != '\n\n' and re.match('[a-zA-Z\-][a-zA-Z\-]{2,}', token.lemma_)]
            #text = [token for token in text if token]
            
#            # implement bigram over the text
#            bigram =iter_bigram(document_loc)
#            text = bigram[text]
            
            
            
#            if (os.path.join(root,fname)) == 'D:/giant/computer/thesis/topic_model/testdata/eq_sm/eq_data\livemint_2018_01_12.txt':
#                print(text)
            
            yield text
            
 
class TxtSubdirsCorpus(object):
    """
    Iterable: on each iteration, return bag-of-words vectors,
    one vector for each document.
 
    Process one document at a time using generators, never
    load the entire corpus into RAM.
 
    """
    def __init__(self, top_dir):
        self.top_dir = top_dir
        # create dictionary = mapping for documents => sparse vectors
        self.dictionary = gensim.corpora.Dictionary(iter_documents(top_dir))
 
    def __iter__(self):
        """
        Again, __iter__ is a generator => TxtSubdirsCorpus is a streamed iterable.
        """
        for tokens in iter_documents(self.top_dir):
            # transform tokens (strings) into a sparse vector, one at a time
            
            yield self.dictionary.doc2bow(tokens)
    
    


            



########## NEW TOPIC ######################
#new_docs = ["Earthquake can be bad. Earthquake in Nepal. People in Nepal are rescued from buildings from Kathmandu "]
#docs = [[word for word in new_doc.lower().split()] for new_doc in new_docs]
#print(docs)
#new_corpus = [dictionary.doc2bow(doc) for doc in docs]
#print(new_corpus)
#lsimodel2 = LsiModel(corpus=new_corpus, num_topics=2, id2word=dictionary)
#pprint.pprint(lsimodel2.show_topics(num_topics=1))

#############################################


####################

#print("###########################")
#hdpmodel = HdpModel(corpus=corpus, id2word=dictionary)
##print(hdpmodel.show_topics())

if __name__ == '__main__':
    
    prj_dir = 'D:/giant/computer/thesis/textmapper/sample/earthquake_nepal'
    text_data_dir = os.path.join(prj_dir,'textdata_sm')
    corpus = build_corpus(text_data_dir) # Build corpus from text data
    
    # location for serailized corpora
    corpora_dir = os.path.join(prj_dir,'corpus_dir')
    if not os.path.exists(corpora_dir):
        os.makedirs(corpora_dir)
    corpora.MmCorpus.serialize(os.path.join(corpora_dir,'SeralizedCorpus.mm'),corpus) # seraialize the corpus
    topic_model  = extract_topic_model(corpus, 'lsi', 10)
    pprint.pprint(topic_model.print_topics())
    
    #pprint.pprint(extract_topics(document_loc))
    #bigram = iter_bigram('D:/giant/computer/thesis/topic_model/testdata/eq_sm')            
    #my_corpus = TxtSubdirsCorpus('D:/giant/computer/thesis/topic_model/testdata/eq_sm')
    #corpora.MmCorpus.serialize('D:/giant/computer/thesis/topic_model/testdata/eq_sm/my_corpus.mm', my_corpus)
    #dictionary = my_corpus.dictionary
    #lsimodel = LsiModel(corpus=my_corpus, num_topics=10, id2word=dictionary)
    #pprint.pprint(lsimodel.show_topics(num_topics=5))
    