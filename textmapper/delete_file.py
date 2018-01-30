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

def filter_link(top_dir):
    g = open(os.path.join(top_dir,'all_links.txt'),'w+')
    for root, dirs, files in os.walk(top_dir):
            for fname in filter(lambda fname: fname.endswith(''), files):
                #
                f = open(os.path.join(root,fname),'r')
                for line in f:
                    if len(line.strip()) != 0:
                        if 'google' not in line and 'youtube' not in line and 'blogger' not in line:
                            g.write(fname[:-5] + ' ' + line)
                f.close()
    g.close()
    


top_dir = r'D:\giant\computer\thesis\textmapper\sample\earthquake_nepal\textdata'
#filter_link(top_dir)
delete_file(top_dir)
#rename_file(top_dir)