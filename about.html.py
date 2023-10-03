#!/usr/bin/python3 
#about.html

import requests as req 
from bs4 import BeautifulSoup as bs 


employee_list=[]

url = 'http://192.168.197.68:8080/about.html'
response = req.get(url)
"""print(response.text)"""
soup = bs(response.text, features='html.parser')

table = soup.find_all('table')

header = soup.find_all('th')

column_title = [title.text.strip() for title in header]

import pandas as pd 

df = pd.DataFrame(columns = column_title)

