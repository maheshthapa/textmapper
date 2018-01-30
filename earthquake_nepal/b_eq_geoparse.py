# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 01:23:54 2018

@author: mahesh
"""

# Geoparses each file in the doc_dir and writes it as geojson and js file


import textmapper as tm

doc_dir = 'D:/giant/computer/thesis/textmapper/sample/earthquake_nepal/textdata'
data_dir = 'D:/giant/computer/thesis/textmapper/sample/earthquake_nepal/map/data'

tm.geoparse_folder(doc_dir,data_dir) # geoparse all docs in doc_dir and write