#! /usr/bin/env python3.4


#from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import sys
import time
## generate page url

def urlopen(url):
	'''
	using requests to replace urllib.requests.urlopen
	return an html
	'''
	headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit     537.36 (KHTML, like Gecko) Chrome"}
	r = requests.get(url, headers=headers)
	return r.text

def generate_pages(subTitle,fromPage,toPage):
	'''
	return  page sites' url list
	'''
	pages = []
	if(fromPage > 0 and fromPage<toPage):
		for i in range(fromPage,toPage+1):
			pages.append('http://www.allitebooks.com'+subTitle+'/page/'+str(i))
	return pages




def get_book_sites_of_one_page(page):
	'''
	get book site's url in one page
	input: page site url
	output: book site urls list
	return book sites in one page
	'''
	html = urlopen(page)
	soup = BeautifulSoup(html,'html.parser')
	linkList = soup.find('main').findAll('a',{'rel':'bookmark'})
	bookSites= []
	for link in linkList[::2]:
		if 'href' in link.attrs:
			#print(link)
			bookSites.append(link.attrs['href'])
	return bookSites


def get_book_urls(bookSite):
	'''
	input a book site
	find book downloading urls in this book site
	then
	return them as a list
	'''
	bookURLs=[]
	html = urlopen(bookSite)
	soup = BeautifulSoup(html,'lxml')
	linkList = soup.findAll("a",{"target":"_blank"})
	for link in linkList:
		if 'href' in link.attrs:
			bookURLs.append(link.attrs['href'])
	return bookURLs    


def get_all_book_urls(fromPage=1, toPage=1, subTitle=''):
	bookSites = []
	bookURLs = []
	pages = generate_pages(subTitle,fromPage, toPage)
	
	for page in pages:
		bookSiteOfOnePage=get_book_sites_of_one_page(page)
		bookSites.extend(bookSiteOfOnePage)
	
	for bookSite in bookSites:
		book_urls=get_book_urls(bookSite)
		bookURLs += book_urls
		
	for bookURL in bookURLs:
		print(bookURL)
		
	#with open(filename, 'w') as f:
	#	f.write(bookURLs)		
	
		
def main():
	if(len(sys.argv) == 4):
		'''
		python getUrl.py 1, 100, programming
		from page 1 to page in subject programming
		'''
		subTitle = str(sys.argv[3])
		fromPage = int(sys.argv[1])
		toPage = int(sys.argv[2])
		get_all_book_urls(fromPage, toPage, subTitle)
	
	if(len(sys.argv) == 3):
		'''
		python getUrl.py 1 100
		from page 1 to page 100
		'''
		subTitle = ''
		fromPage = int(sys.argv[1])
		toPage = int(sys.argv[2])
		#filename = subTitle="-"+str(pageNum)+".txt"
		get_all_book_urls(fromPage, toPage, subTitle)
		
	elif(len(sys.argv) == 2):
		'''
		python getUrl.py 10
		from page 10 to page 10
		only download books on page 10
		'''
		fromPage = int(sys.argv[1])
		toPage = fromPage + 1
		subTitle = ''
		#filename = "All-"+str(pageNum)+".txt"
		get_all_book_urls(fromPage, toPage, subTitle)
		
	elif(len(sys.argv)== 1):
		fromPage = 1
		toPage = 2
		subTitle = ''
		
		#filename = "All-"+"1"+"-"+time.strftime('%Y-%m-%d', time.localtime())+".txt"
		get_all_book_urls(fromPage, toPage, subTitle)
	else:
		print("Error, too many arguments")
		
	
	
if __name__ == '__main__':
	
	#filename = ''
	main()
	
	

		
		
		

