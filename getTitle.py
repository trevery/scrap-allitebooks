#! /usr/bin/env python3
# -*- coding: utf-8 -*-


from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def getTitle(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	try:
		bsObj = BeautifulSoup(html.read())
		title = bsObj.h1.get_text()
	except AttributeError as e:
		return None
	return title                                               


url = input("Your url: ")
title = getTitle(url)


if title == None:
	print("Title could not be found")
else:
	print(title)
		
		
