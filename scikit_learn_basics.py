# -*- coding: utf-8 -*-
"""
Created on Tue Jun 09 14:45:41 2015

@author: Subu Ganesh
"""

from sklearn.datasets import fetch_20newsgroups
newsgroups_train = fetch_20newsgroups(subset='train')

print newsgroups_train.target_names
print len(newsgroups_train.filenames)

for t in newsgroups_train.target[:10]:
    print (str(newsgroups_train.target_names[t])+'\n')
    
    