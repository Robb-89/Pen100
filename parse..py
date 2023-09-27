#!/usr/bin/python3

from bs4 import BeautifulSoup 
import requests 

url = "http://192.168.169.68:8080/table/"

page = requests.get(url)
soup = BeautifulSoup(page.text, features='html.parser')

print(soup)