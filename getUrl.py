#! /usr/bin/env python3.4


#from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup

## generate page url

def urlopen(url):
	'''
	using requests to replace urllib.requests.urlopen
	return an html
	'''
	headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit     537.36 (KHTML, like Gecko) Chrome"}
	r = requests.get(url, headers=headers)
	return r.text

def generate_pages(subTitle,pageNum):
	'''
	return  page sites' url list
	'''
	pages = []
	for i in range(1,pageNum+1):
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


def get_book_url(bookSite):
	'''
	input a book site
	find book downloading urls in this book site
	then
	return it
	'''
	html = urlopen(bookSite)
	soup = BeautifulSoup(html,'lxml')
	bookUrl = soup.find("a",{"target":"_blank"}).attrs['href']
	return bookUrl    


def get_all_book_urls(pageNum=1,subTitle=''):
	bookSites = []
	pages = generate_pages(subTitle,pageNum)
	
	for page in pages:
		bookSiteOfOnePage=get_book_sites_of_one_page(page)
		bookSites.extend(bookSiteOfOnePage)
	
	for bookSite in bookSites:
		bookUrl = get_book_url(bookSite)
		print(bookUrl)
		
		
def main():
	get_all_book_urls()
	
if __name__ == '__main__':
	
	main()
	
	

		
		
		

