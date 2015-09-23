# -*- coding: utf-8 -*-
"""
Created on Thu Jun 04 15:56:45 2015

@author: Subu Ganesh
"""
import re

file_reader = open('fullReviews_Cleaned.txt')

links = []
link_set = set()

for line in file_reader:
    line = line.strip().split('##')
    link = line[3]
    links.append(link)            
    movie_link = 'http://www.rottentomatoes.com/'+link    
    link_set = set(links)
        
    print movie_link

print 'set',len(link_set)
print  'list', len(links) 

file_reader.close()
file_writer = open('links_unique')
for items in link_set:
    file_writer.write(items+'\n')
file_writer.close()
