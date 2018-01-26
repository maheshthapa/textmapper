# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 15:13:15 2018

@author: mahesh
"""
import pprint

from nltk.corpus import wordnet




 
 
def convert_to_humanreadable(topics):
    """
    Converts topics to human readable format
    
    """
    for i, topic in enumerate(topics):
        topics[i] = list(topic)
        topics[i][1] = tuple([w for w in topic[1].split('"') if wordnet.synsets(w)])
        topics[i] = tuple(topics[i])
        
    return(topics)
    

if __name__ == '__main__':
    topics = [(0,
  '0.396*"nepal" + 0.314*"earthquake" + 0.284*"people" + 0.183*"kathmandu" + '
  '0.160*"quake" + 0.133*"day" + 0.128*"village" + 0.123*"government" + '
  '0.123*"house" + 0.116*"country"'),
 (1,
  '-0.361*"earthquake" + -0.246*"nepal" + 0.201*"day" + 0.153*"house" + '
  '0.153*"camp" + 0.151*"dan" + -0.136*"building" + 0.135*"village" + '
  '0.134*"people" + 0.128*"find"'),
 (2,
  '0.288*"nepal" + -0.265*"earthquake" + -0.235*"quake" + 0.201*"government" + '
  '-0.188*"camp" + 0.184*"need" + -0.173*"everest" + 0.146*"aid" + '
  '-0.145*"climber" + -0.140*"building"'),
 (3,
  '0.416*"quake" + 0.253*"kathmandu" + -0.245*"earthquake" + 0.215*"child" + '
  '-0.176*"camp" + -0.171*"climber" + 0.133*"district" + -0.127*"nepal" + '
  '-0.122*"base" + 0.120*"april"'),
 (4,
  '-0.277*"barpak" + -0.277*"james" + -0.277*"nachtwey" + -0.221*"village" + '
  '-0.220*"time" + -0.190*"nepal" + 0.178*"government" + 0.146*"disaster" + '
  '0.146*"need" + -0.140*"gurung"'),
 (5,
  '-0.325*"camp" + -0.247*"child" + 0.219*"kathmandu" + -0.197*"climber" + '
  '0.188*"building" + 0.179*"earthquake" + -0.143*"price" + -0.123*"woman" + '
  '-0.117*"york" + -0.117*"new"'),
 (6,
  '0.311*"lake" + -0.256*"building" + 0.249*"glacial" + 0.201*"government" + '
  '0.194*"sherpa" + -0.177*"child" + 0.162*"image" + 0.136*"glacier" + '
  '0.130*"everest" + -0.126*"earthquake"'),
 (7,
  '0.418*"child" + 0.224*"lake" + 0.201*"school" + 0.177*"glacial" + '
  '-0.165*"people" + -0.154*"aid" + 0.146*"woman" + 0.136*"sherpa" + '
  '-0.131*"price" + -0.111*"york"'),
 (8,
  '-0.234*"damage" + 0.212*"price" + -0.197*"camp" + 0.193*"new" + '
  '-0.190*"climber" + 0.185*"building" + 0.176*"lake" + 0.175*"york" + '
  '0.172*"giles" + 0.164*"times"'),
 (9,
  '0.199*"damage" + 0.175*"disaster" + 0.147*"lake" + 0.146*"price" + '
  '-0.144*"building" + -0.138*"kathmandu" + 0.135*"sector" + -0.131*"camp" + '
  '-0.131*"child" + 0.127*"new"')]
    
    
    hrt = convert_to_humanreadable(topics)
    pprint.pprint(hrt)


