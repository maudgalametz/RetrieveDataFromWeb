import os
import csv
import requests
import pandas
import urllib2
import re
from requests.auth import HTTPBasicAuth
from lxml import html
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from urllib2.request import urlopen as uReq

GCcode = "GC7H3ZP"
MyIdentifier = #put your username here
MyPassword = #put your pwd here


# Login on the geocaching website
url = 'https://www.geocaching.com/account/signin?returnUrl=%2fplay'
driver = webdriver.Firefox()
driver.get(url)
driver.find_element_by_id("UsernameOrEmail").send_keys(MyIdentifier)
driver.find_element_by_id ("Password").send_keys(MyPassword)
driver.find_element_by_id ("SignIn").click()

# Use BeautifulSoup to read the webpage
url = 'https://coord.info/'+GCcode+'.html'
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# if page has a well-defined table
#tables = pd.read_html('https://coord.info/'+GCcode+'.html')
#print(tables[0])


# Extract the logs and treat the 1st and last element
text = soup.get_text()
pos1 = text.find('{"LogID"')
pos2 = text.find('], "pageInfo"')
text = text[pos1:pos2] 
l = text.split('},"Images":[]},{')
l[4] = l[4].replace('},"Images":[]}','') 
l[0] = l[0].replace('{"LogID"','"LogID"') 

# Count the number of logs
count = text.count('UserName')
print GCcode, "Found by ", str(count), "geocachers"


# Save the log table in a csv file
with open('/Users/mgalamet/Desktop/test.csv', 'w') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter='\t',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
	# Read the tags and save them
	nametag = []
	l2 = l[0].split(',"')
	for i in range(len(l2)):
		l3 = l2[i].split(':')
		nametag.append(l3[0].replace('"',''))
	spamwriter.writerow(nametag)
	# Save the lines
	for i in range(len(l)):
		l2 = l[i].split(',"')
		valuet = []	
		for j in range(len(l2)):
			l3 = l2[j].split(':')
			if (l3[0] == 'LogText"'):
				l3[1] = ""
			valuet.append(l3[1].encode('utf-8'))
		spamwriter.writerow(valuet)


# Query the data

#Read the saved table
data = pandas.read_csv('/Users/mgalamet/Desktop/test.csv', names=nametag, skiprows=1, delimiter='\t',dtype=None)

#Clean the geocacher list
df = data.drop(data.query('LogType=="Write note"').index)
df = df.drop(df.query('LogType=="Owner Maintenance"').index)
df = df.drop(df.query('UserName=="assistantGCfr"').index)

print df['UserName']


