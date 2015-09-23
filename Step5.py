# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 15:07:24 2015

@author: Subu Ganesh
"""

#file_opener = open('movieDetails_Full.txt')
file_opener_40 = open('RT_CrititcReviewsFullWithRatingGreaterthan40.txt')
file_writer = open('step5_reviewer.txt','w')
count = 0
for lines in file_opener_40:
    line = lines.strip()    
    line = line.split('##')
    reviewer = line[6]
    rating = line[7]
    movie_name_full = line[3].split('/')[2]
    file_writer.write(str(reviewer+' '+movie_name_full+' '+rating+'\n'))
    count = count + 1
    print count

file_opener_40.close()
file_writer.close()
