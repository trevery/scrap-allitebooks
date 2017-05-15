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

def getDetail(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	try:
		bsObj = BeautifulSoup(html.read())
		detail = bsObj.find("div",{"class":"book-detail"}).get_text()
	except AttributeError as e:
		return None
	return detail        
	
	
def getDownloadLink(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	try:
		bsObj = BeautifulSoup(html.read())
		downloadLink = bsObj.find("a",{"target":"_blank"}).attrs['href']
	except AttributeError as e:
		return None
	return downloadLink  
	
def getDescription(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	try:
		bsObj = BeautifulSoup(html.read())
		bookDescription = bsObj.find("div",{"class":"entry-content"}).get_text()
	except AttributeError as e:
		return None
	return bookDescription 

if __name__ == '__main__':

	#url = input("Your url: ")
	url = ("http://www.allitebooks.com/arduino-blink-blueprints")
	title = getTitle(url)
	detail = getDetail(url)
	downloadLink = getDownloadLink(url)
	bookDescription = getDescription(url)


	if title == None:
		print("Title could not be found")
	elif detail == None:
		print("Detail could not be found")
	elif downloadLink == None:
		print("Download link could not be found")
	elif bookDescription == None:
		print("Book Description could not be found")
	else:
		print("title:\n"+title)
	#	print("--------------")
	#	print("book detail:\n"+detail)
	#	print(bookDescription	)
		print("downloadLink:\n"+downloadLink)
	
