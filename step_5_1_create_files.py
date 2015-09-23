# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 21:10:00 2015

@author: Subu Ganesh
"""

reviewer_dict = dict()
file_opener_review = open('step5_reviewer.txt')
#file_opener_movie = open('step4_results_final.txt')
for lines in file_opener_review:
    line = lines.strip()
    line = line.split(' ')
    movie_name = line[1]
    reviewer_name = line[0]
    #review = line[2]
    #print reviewer_name
    if reviewer_name not in reviewer_dict:
        file_writer = open('E:\\Stevens_sem2\\Research_work\\reviewer_documents\\'+reviewer_name+'.txt','w')
        file_writer.close()
        print reviewer_name
    else:
        continue
file_opener_review.close()