from myCourses import s, d
from grabbingAssignments import d2
import os
import makingDirectories
from bs4 import BeautifulSoup
import urllib
import time

import requests

for i in d2.keys():
    path = "C:\\Users\\user-name\\Desktop\\Moodle\\" + i   #path of your Desktop with the directory Moodle specified
                                                           #change the directory name as per your wish

    os.chdir(path)
    for j in d2[i]:
        for k in j:
            url = k["href"]
            name = k.text
            dirs = os.listdir(path)
            if name not in dirs:
                
                r = s.get(url)    
                
                with open(name,'wb') as f:
                    
                    for chunk in r.iter_content(1024 * 1024 * 2):  # 2 MB chunks
                        f.write(chunk)
