# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 01:55:01 2018

@author: mahesh
"""

import json
from gensim import models, corpora
import textmapper as tm


data_file = 'D:/giant/computer/thesis/textmapper/sample/earthquake_nepal/map/data/geodata.json'
output_json_file = 'D:/giant/computer/thesis/textmapper/sample/earthquake_nepal/map/data/geo_prob_data.json'
output_js_file = 'D:/giant/computer/thesis/textmapper/sample/earthquake_nepal/map/data/geo_prob_data.js'
topic_model_file = 'D:/giant/computer/thesis/textmapper/sample/earthquake_nepal/corpus_dir/topic_model.model'
dictionary_file = 'D:/giant/computer/thesis/textmapper/sample/earthquake_nepal/corpus_dir/corpus.dict'


tm.topic_score(data_file, output_json_file, output_js_file, topic_model_file,dictionary_file)
    
