#! /usr/bin/env python3

#Author: Can
#Purpose: get pdf Url from Allitebooks.com

from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re


random.seed(datetime.datetime.now())
def getLinks(url):
	html = urlopen(url)
	bsObj = BeautifulSoup(html)
	urlList = bsObj.findAll("a",href=re.compile(".*"))
	print("urlList:")
	print(" ")
	return urlList
						
linksList = getLinks("http://www.allitebooks.com/ " +
						input("Your url: http://www.allitebooks.com/"))
while len(linksList) > 0:
	newLink = linksList[random.randint(0, len(linksList)-1)].attrs["href"]
	#if newlink == re.compile("http://file.*.pdf"):
	print(newLink)
	linksList = getLinks(newLink)

