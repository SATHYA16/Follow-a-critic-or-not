# -*- coding: utf-8 -*-
"""

This script downloads the html files for critics in the rotten tomatoes database. 


"""

import urllib2
import re
import string, os,sys,time


write_folder = 'criticpages'

#To create a new folder to save the critic pages
if not os.path.exists(write_folder):
    os.mkdir(write_folder)

# iterate for all the critics from a through z
for alphabet in list(string.ascii_lowercase)[:12]:
    criticsListURL = 'http://www.rottentomatoes.com/critics/authors?view=3&letter='+alphabet
    print criticsListURL
    write_folder = alphabet
    if not os.path.exists(write_folder):
        os.mkdir(write_folder)    
# creates a browser to load the data
    browser = urllib2.build_opener()
    browser.addheaders=[('User-agent', 'Mozilla/5.0')]
    response = browser.open(criticsListURL)
# Saves the HTML file content in the object
    myHTML = response.read()
    criticsList = re.finditer('20px;"> <a href="(.*?)" class="">',myHTML)
    
    count = 0 
    print count
# iterares for each critic in the a page and downloads the page
    for critics in criticsList:
        start = time.time()        
        critic = critics.group(1)
        pageNumber = 1             
        while pageNumber >=  1:
            criticURL = 'http://www.rottentomatoes.com'+critic+'?cats=&genreid=&letter=&switches=&sortby=&limit=50&page='+str(pageNumber)
            count = count + 1
            print criticURL+critic , count
            filename = critic[8:critic.rfind('/')]+'_'+str(pageNumber)+'.html' 
            print filename
            browser_one = urllib2.build_opener()
            browser_one.addheaders=[('User-agent', 'Mozilla/5.0')]
            reviewResponse = browser_one.open(criticURL)
            myHTML_review= reviewResponse.read()
            #reviewsPerPage = re.search('Showing(.*?)-(.*?)of(.*?)</div',myHTML_review).group(2)
            #totalReviews = re.search('Showing(.*?)-(.*?)of(.*?)</div',myHTML_review).group(3)
            nextButton = re.search('<a href=".*?">Next</a>',myHTML_review,re.S)
            print type(nextButton), nextButton
            file_writer = open(write_folder+'/'+filename,'w')
            file_writer.write(myHTML_review)
            file_writer.close()
            if nextButton is not None :
                pageNumber = pageNumber + 1
            else:
                break
        end = time.time()
        diff = end - start
        print critic , diff
        #pages = int(totalReviews)/
    
        
        