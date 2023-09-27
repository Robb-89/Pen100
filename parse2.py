#!/usr/bin/python3

from bs4 import BeautifulSoup as bs 
import requests 


url = "http://192.168.169.68:8080/table/"


response = requests.get(url)
soup = bs(response.text, features='html.parser')

print(response.status_code)

flag=[]

table = soup.find('table', class_= 'container')


for data in soup.find_all('tbody'):
    rows = data.find_all('tr')



for row in rows:
    name = row.find_all('td')[0].text


flag.append(rows)

print(flag)