from myCourses import driver, d
from grabbingAssignments import d2
import os
import makingDirectories
from bs4 import BeautifulSoup
import urllib
import time

import requests

for i in d2.keys():
    path = "C:\\Users\\sankalpjain\\Desktop\\Moodle\\" + i
    os.chdir(path)
    for j in d2[i]:
        for k in j:
            url = k["href"]
            name = k.text
            dirs = os.listdir(path)
            if name not in dirs:
                driver.get(name)
                """with open(name,'wb') as f:
                    print(name)"""
