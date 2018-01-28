# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 21:54:27 2018

@author: mahesh
"""
import os 

# Delete file larger and smaller than particular size

def delete_file(top_dir):
    
    # Delete file larger and smaller than particular size
    for root, dirs, files in os.walk(top_dir):
            for fname in filter(lambda fname: fname.endswith(''), files):
                doc = os.path.join(root,fname)
                if (os.path.getsize(doc) < 3000) or (os.path.getsize(doc) > 8000):
                    os.remove(doc)

def rename_file(top_dir):
    for root, dirs, files in os.walk(top_dir):
            for fname in filter(lambda fname: fname.endswith(''), files):
                doc = os.path.join(root,fname) 
                doc_new = doc + '.txt'
                os.rename(doc, doc_new)
#                print(os.path.join(doc,fname + '.txt'))
#                os.rename(doc,os.path.join(doc,fname + '.txt'))


top_dir = r'D:\giant\computer\thesis\textmapper\sample\earthquake_nepal\textdata'
delete_file(top_dir)
#rename_file(top_dir)