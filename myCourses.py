
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from bs4 import BeautifulSoup
driver = webdriver.Chrome()
driver.set_window_size(1024, 768)

from getpass import getpass
urls = ['https://moodlecc.vit.ac.in/login/index.php']
driver.get(urls[0])

username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")

username.send_keys("UserName")
password.send_keys("Password")

driver.find_element_by_id("loginbtn").click()

dashboard = 'http://moodlecc.vit.ac.in/?redirect=0'
driver.get(dashboard)
r = driver.page_source

soup = BeautifulSoup(r, 'html.parser')
divTag = soup.find_all("div", {"class": "courses frontpage-course-list-enrolled"})
l = []
for tag in divTag:
    tdTags = tag.find_all('a')
    for tag in tdTags:
        if tag["href"].startswith("https://moodlecc.vit.ac.in/course/view.php?id"):
            l.append(tag)
d = {}
l1 = []
for i in l:
    d[i["href"]] = i.text
for i in d.values():
    l1.append(i)

