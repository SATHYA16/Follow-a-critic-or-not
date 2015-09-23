# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 16:03:35 2015

@author: Subu Ganesh
"""

count_dict = dict()
count40_dict = dict()
count40_names = []

file_opener = open('RT_CrititcReviewsFullWithRating.txt')
file_writer_gt40 = open('RT_CrititcReviewsFullWithRatingGreaterthan40.txt','w')
file_writer_lt40 = open('RT_CrititcReviewsFullWithRatingLessthan40.txt','w')

for lines in file_opener:
    lines = lines.rstrip()    
    line = lines.split('##')
    reviewer_name = line[6]
    if reviewer_name not in count_dict:
        count_dict[reviewer_name] = 1
    else: 
        count_dict[reviewer_name] = count_dict[reviewer_name] + 1

for names in count_dict:
    if count_dict[names] > 40 :
        count40_dict[names] = count_dict[names]
        count40_names.append(names)

print count40_names
file_opener.close()
file_opener = open('RT_CrititcReviewsFullWithRating.txt')
count = 0
for lines in file_opener:
    lines = lines.rstrip()
    line = lines.split('##')
    reviewer_name = line[6]
    count = count + 1    
    print reviewer_name, count     
    if reviewer_name in count40_names:
        file_writer_gt40.write(lines+'\n')
    else:
        file_writer_lt40.write(lines+'\n')
      
    

file_writer_gt40.close()
file_writer_lt40.close()
file_opener.close()