# -*- coding: utf-8 -*-
"""
Description: 
"""

import urllib2
import re
import string

for alphabet in range(1,3):#list(string.ascii_lowercase):
    criticsListURL = 'http://www.rottentomatoes.com/critics/authors?view=3&letter=a'#+alphabet
    print criticsListURL
    browser = urllib2.build_opener()
    browser.addheaders=[('User-agent', 'Mozilla/5.0')]
    response = browser.open(criticsListURL)
    myHTML = response.read()
    criticsList = re.finditer('20px;"> <a href="(.*?)" class="">',myHTML)

    count = 0    
    for critics in criticsList:
        critic = critics.group(1)
        criticURL = 'http://www.rottentomatoes.com'+critic+'?cats=&genreid=&letter=&switches=&sortby=&limit=50&page='
        count = count + 1
        print 'http://www.rottentomatoes.com'+critic , count
        browser_one = urllib2.build_opener()
        browser_one.addheaders=[('User-agent', 'Mozilla/5.0')]
        reviewResponse = browser_one.open(criticURL)
        myHTML_review= reviewResponse.read()
        singles = re.finditer('<span class="icon(\w*?)" title="(.*?)"></span>.*?class="tMeterIcon.*?<span class="tMeterScore">(...?)</span>.*?data-pageheader=""href="(.*?)">(.*?)</td>.*?<a href="(.*?)"target="_blank"rel="nofollow"class="unstyled articleLink"></a>')
        
