# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 21:41:43 2015

@author: Subu Ganesh
"""
import glob,re
file_opener_reviewer = open('step4_results_final_sample.txt')
file_opener_movie = open('step4_results_final.txt')
reviewer_dict = dict()
movie_content = file_opener_movie.read()
for lines in file_opener_reviewer:
    line = lines.strip()
    line = line.split(' ')
    movie_name = line[1]
    reviewer_name = line[0]
    movie_rating = line[2]
    
    for file_name in glob.glob('*.txt'):
        if file_name ==  reviewer_name:
            file_writer = open(file_name,'w')
            movie_line = re.search(movie_name+'(.*?)\n',movie_content).group(0)
            file_writer.write(str(movie_line+' '+movie_rating+'\n'))
            file_writer.close()

