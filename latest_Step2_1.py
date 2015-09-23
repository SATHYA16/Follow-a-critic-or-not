# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 16:02:43 2015

@author: Subu Ganesh
"""
np_score_dict = dict()
pn_score_dict = dict()
movie_details = dict()

file_opener_movies = open('E:\\Stevens_sem2\\Research_work\\Copy of RT_movie_Step4.txt')
fie_opener_np_pn = open('E:\\Stevens_sem2\\Research_work\\RT_movies__np_pn_score.txt')

for lines in fie_opener_np_pn:
    line = lines.strip().split('##')
    movie_np_pn = line[0]
    np_score = line[1]
    pn_score = line[2]
    if movie_np_pn not in np_score_dict and  movie_np_pn not in pn_score_dict:
        np_score_dict[movie_np_pn] = np_score
        pn_score_dict[movie_np_pn] = pn_score

print 'dictionary done'

file_writer_np = open('np_document.txt','w')
file_writer_pn = open('pn_document.txt','w')

for lines in file_opener_movies:
    lines = lines.strip()    
    line = lines.split('##')
    movie_name = line[0]
    document = line[1]
    if movie_name in np_score_dict and movie_name in pn_score_dict:
        print movie_name        
        file_writer_np.write(str(movie_name) + ' '+str(document)+' ' +'##'+str(np_score_dict[movie_name])+'\n')
        file_writer_pn.write(str(movie_name) + ' '+str(document)+' ' +'##'+str(pn_score_dict[movie_name])+ '\n')

file_writer_np.close()
file_writer_pn.close()
file_opener_movies.close()
fie_opener_np_pn.close()
        
        
        
    
    
    
    