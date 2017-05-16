#! /usr/bin/env python3.4


from urllib.request import urlopen
from bs4 import BeautifulSoup

## generate page url

def generatePageUrl(subTitle,pageNum):
	pageUrlList = []
	for i in range(1,pageNum+1):
		pageUrlList.append('http://www.allitebooks.com'+subTitle+'/page/'+str(i))
	return pageUrlList


def getBookUrlInThisPage(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	try:
		bsObj = BeautifulSoup(html)
		linkList = bsObj.find('main').findAll('a',{'rel':'bookmark'})
	except AttributeError as e:
		return None
		
	bookUrlListInThisPage= []
	for link in linkList[::2]:
		if 'href' in link.attrs:
			bookUrlListInThisPage.append(link.attrs['href'])
	return bookUrlListInThisPage

def getPdfUrl(bookUrl):
	try:
		html = urlopen(bookUrl)
	except HTTPError as e:
		return None
	try:
		bsObj = BeautifulSoup(html.read())
		pdfUrl = bsObj.find("a",{"target":"_blank"}).attrs['href']
	except AttributeError as e:
		return None
	return pdfUrl    
	
	
if __name__ == '__main__':
	
	pageNum = 2
	subTitle = ''

	bookUrlList = []
	pageUrlList = generatePageUrl(subTitle,pageNum)
		
	for pageUrl in pageUrlList:
		bookUrlList.extend(getBookUrlInThisPage(pageUrl))
	for bookUrl in bookUrlList:
		print(getPdfUrl(bookUrl))
		
		
		

