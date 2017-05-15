
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup



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

url = input("Your url: ")
detail = getDetail(url)


if detail == None:
	print("Detail could not be fonud")
else:
	print(detail)		
