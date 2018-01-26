# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 13:54:27 2018

@author: mahesh
"""
import requests, json
import os

# geojson structure
geoobject = {
  "type": "FeatureCollection",
  "properties": {
    "apiVersion": "0.5.1",
    "source": "geoparser.io",
    "id": "KbjJB4TX4Exu2oLJ8JaD"
  },
  "features": []
}

def geoparse_text(text):
    url = 'https://geoparser.io/api/geoparser'
    headers = {'Authorization': 'apiKey 04879088639590257'}
    #data = {'inputText': 'I was born in Springfield and grew up in Boston.'}
    data = {'inputText': text}
    response = requests.post(url, headers=headers, data=data)
    #print (json.dumps(response.json(), indent=4))
    geostring = json.dumps(response.json())
    return geostring

def get_latlong(geoobject):
    """
    Not used currently.
    """
    features = geoobject['features']
    entities = []
    for feature in features:
        name = feature['properties']['name']
        location = tuple(feature['geometry']['coordinates'])
        entity =  (name, location)
        entities.append(entity)
    return entities

def geoparse_folder(doc_dir,data_dir):
    for root, dirs, files in os.walk(doc_dir):
        for fname in filter(lambda fname: fname.endswith('.txt'), files):
            # read each document as one big string
            f = open(os.path.join(root, fname)).read()
            #print(fname)
            # Geoparse the files and get the locations
            response_string = geoparse_text(f) # Is String
            
            
            response_object = json.loads(response_string) #Conver to object
            locations = response_object["features"]
            
            features = geoobject["features"]
            # Append the locations to geoobject
            for loc in locations:
                location_list =  [w['properties']['name'] for w in features]
                if loc['properties']['name'] not in location_list:
                    geoobject["features"].append(loc)
                
     # Write the geoparsed data as js
    loc_file = open(os.path.join(data_dir,'geodata.json'),'w+')
    loc_file.write ('geoobjects =')
    loc_file.write(json.dumps(geoobject))
    loc_file.close()
    
    # Write the geoparsed data as json
    loc_file = open(os.path.join(data_dir,'geodata.json'),'w+')
    loc_file.write(json.dumps(geoobject))
    loc_file.close()
    
                
    
            
            
    

#print(data['features'][0]['geometry']['coordinates'])
if __name__ == '__main__':
    sent = 'I was born in Springfield and grew up in Boston.'
    response = (geoparse_text(sent))
    response_object = json.loads(response)["features"]
    print(response_object)
    