# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 01:55:01 2018

@author: mahesh
"""

import json
from gensim import models, corpora


def fill_list(feature, topic_probability,topic_model):
    """
    fills the vacant positions of topic probability with (topic_number, 0)
    """
    num_topics = topic_model.num_topics
    if len(topic_probability) == 0:
        topic_probability = [(w,0) for w in range(num_topics)]
        feature["topic_probability"] = topic_probability
    else:    
        last_item_index = topic_probability[-1][0] 
        #print(last_item_index)
        for i in range(last_item_index):
            if topic_probability[i][0] == i:
                pass
                #print(topic_probability)
            else:
                topic_probability.insert(i,(i,0))
                #print(topic_probability)
                
        for j in range(last_item_index + 1, num_topics):
            topic_probability.append((j,0))
   
    return topic_probability

def topic_score(data_file, output_json_file, output_js_file, topic_model_file,dictionary_file):
    """
    Creates a new file with probability score of each topic.
    data_file = existing geojson file
    data_score_file = new file 
    """
    # Create a new file for writing the geosjson file with topic_probability
    #data_score_file = 'D:/giant/computer/thesis/textmapper/sample/earthquake_nepal/map/data/geo_prob_data.json'
    g = open(output_json_file,'w+')
    
    # Open geojson data file and load the geojson data
    #data_file = 'D:/giant/computer/thesis/textmapper/sample/earthquake_nepal/map/data/geodata.json'
    f = open(data_file,'r')
    data = json.load(f)
    
    #load topic model
    #topic_model = models.LdaModel.load('D:/giant/computer/thesis/textmapper/sample/earthquake_nepal/corpus_dir/topic_model.model')
    topic_model = models.LdaModel.load(topic_model_file)
    #dictionary = corpora.Dictionary.load('D:/giant/computer/thesis/textmapper/sample/earthquake_nepal/corpus_dir/eq.dict')
    dictionary = corpora.Dictionary.load(dictionary_file)
    num_topics = topic_model.num_topics
    #topic_model.show_topics(num_topics)
    
    
    
    # Add the list of  topic probability to feature key
    for feature in data['features']:
        loc_term = (feature['properties']['name']).lower() # get the name of the location and in lower case
        if dictionary.token2id.get(loc_term,0): # if does not exits, defaults to 0
            
            topic_probability = topic_model.get_term_topics(loc_term, 0)
            topic_probability = fill_list(feature, topic_probability,topic_model)
            feature["topic_probability"] = topic_probability
            print(feature['topic_probability'])
        else:
            topic_probability = [(w,0) for w in range(num_topics)]
            feature["topic_probability"] = topic_probability
            
       
    
       
    # Write the data (done with probability score) into json file
    g.write(json.dumps(data))
    g.close()
    
    f.close()
    
    # Write the data in js file with header 'geoobjects='
    #loc_file = open('D:/giant/computer/thesis/textmapper/sample/earthquake_nepal/map/data/geo_prob_data.js','w+')
    loc_file = open(output_js_file,'w+')
    loc_file.write ('geoobjects =')
    loc_file.write(json.dumps(data))
    loc_file.close()

if __name__ == '__main__':
    print('from file')