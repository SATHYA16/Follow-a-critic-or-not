# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 14:55:22 2015

@author: Subu Ganesh
"""

file_opener = open('RT_CriticReviewsFull.txt')
file_writer = open('RT_CrititcReviewsFullWithRating.txt','w')
pos_rating = ['A','A-','A+','B+']
neg_rating = ['C-','D+','D-','D']
count = 0
for lines in file_opener:    
    lines = lines.rstrip()    
    line = lines.strip().split('##')
    rating = line[1]
    count = count +1
    print rating, count
    if rating.find('/') is not -1 :     
        try:        
            score = float(rating[0:rating.find('/')])/float(rating[rating.find('/')+1:len(rating)])
        #print score
        except ValueError:
            continue
        except ZeroDivisionError:
            file_writer.write(str(lines+'##'+'0'+'\n'))
        if score <=0.4:
            file_writer.write(str(lines+'##'+'0'+'\n'))
        elif score >= 0.7:
            file_writer.write(str(lines+'##'+'1'+'\n'))
    #elif rating.find('A') or rating.find('A-') or rating.find('A') or rating.find('B+'):
    elif rating in pos_rating:
        file_writer.write(str(lines+'##'+'1'+'\n'))
    elif rating in neg_rating:
        file_writer.write(str(lines+'##'+'0'+'\n'))
    
file_opener.close()
file_writer.close()