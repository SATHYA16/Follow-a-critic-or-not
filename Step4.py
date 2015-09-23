# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 15:07:24 2015

@author: Subu Ganesh
"""

file_opener = open('movieinfo_HTML_data_v1.txt')
file_writer = open('step4_results_final.txt','w')
count = 0
for lines in file_opener:
    
    directors= []
    director_count = 0
    writer_count = 0
    actor_count = 0
    line = lines.strip()
    line = line.split('##')    
    movie_name = file_writer.write(str(line[0])+' ')
    movie_description = file_writer.write(str(line[1])+' ')
    rating = file_writer.write('rating_'+str(line[2])+' ')
    genre = file_writer.write('genre_'+str(line[3])+' ')
    for director in line[4].split(','):
        director_count = director_count + 1
        if director_count != len(line[4].split(',')):
            file_writer.write('director_'+str(director)+' ')
        else:
            file_writer.write('director_'+str(director))
    file_writer.write(' ')
    for writer in line[5].split(','):
        writer_count = writer_count + 1
        if writer_count != len(line[5].split(',')):
            file_writer.write('director_'+str(writer)+' ')
        else:
            file_writer.write('director_'+str(writer))
    file_writer.write(' ')
    for actor in line[10].split(','):
        actor_count = actor_count + 1
        if actor_count != len(line[10].split(',')) :
            file_writer.write('actor_'+str(actor)+' ')
        else:
            file_writer.write('actor_'+str(actor))
    file_writer.write(' ')
    date = line[6]
   # year = line[5].split(',')
    if date.startswith(' May') or date.startswith(' Jun') or date.startswith(' Jul') or date.startswith(' Aug') :
        season = 'Summer'
        year = line[6].split(',')
        year_new = year[1][1:5]
    elif date.startswith(' Sep') or date.startswith(' Oct') or date.startswith(' Nov'):
        season = 'Fall'
        year = line[6].split(',')
        year_new = year[1][1:5]
    elif date.startswith(' Dec') or date.startswith(' Jan') or date.startswith(' Feb'):
        season = 'Winter'
        year = line[6].split(',')
        year_new = year[1][1:5]
    elif date.startswith(' Mar') or date.startswith(' Apr') :
         season = 'Spring'
         year = line[6].split(',')
         year_new = year[1][1:5]
    elif date.startswith('NA'):
        season = 'NA'
        year_new = season
    else:
        season = date
    file_writer.write('released_'+season+' ')
    file_writer.write('year_released_'+str(year_new)+'\n')    
    count = count + 1
    print count    
    
file_writer.close()

    
    
    