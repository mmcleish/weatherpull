#!/usr/bin/python3
#v1
#import lib
import urllib2
#import bs4 from 
from bs4 import BeautifulSoup


page = 
requests.get('https://weather.gc.ca/city/pages/on-25_metric_e.html', 
verify=False)
soup = BeautifulSoup(page.content, html.parser')
print(soup.title)


#url scrape
#weather = "https://weather.gc.ca/city/pages/on-25_metric_e.html"
#query
#page = urllib2.urlopen(weater)
#parse
#soup = BeautifulSoup(page, `html.parser`)
#print soup
