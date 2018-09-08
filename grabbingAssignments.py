import mechanicalsoup
import requests
from bs4 import BeautifulSoup
import re

from myCourses import s, d

l = d.keys()
d2 = {}


for key in l:  
    link = key
    r1 = s.get(link)
    r1 = r1.text
    soup = BeautifulSoup(r1, 'html.parser')
    
    d1 = {}
    divTag = soup.findAll('a', attrs={'href': re.compile("^http://moodlecc.vit.ac.in/mod/assign/view")})
   
    for i in divTag:
        d1[i['href']] = i.text
   
    l1 = []
    for i in d1.keys():
        r2 = s.get(i)
        r2 = r2.text
        soup = BeautifulSoup(r2, 'html.parser')
        divTag1 = soup.findAll('a', attrs={'href': re.compile("^http://moodlecc.vit.ac.in/pluginfile.php/[0-9]+/mod_assign/")})

        if len(divTag1) > 0:
            l1.append(divTag1)
        d2[d[key]] = l1


