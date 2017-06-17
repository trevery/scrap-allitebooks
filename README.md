# scrap-allitebooks
a python crawler to scrap books' downloading urls from allitebooks.com

## requirements
I use BeautifulSoup library to parse html, so you need to install it.
If you have installed, congratulations! If you have not, this [page](https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#id8)will help.


## How to use it?

0. The easiest way to use this repo, is Just open the bookUrl category, and you will find the urls i have scraped. Use the downloading tools such as "Thunder(迅雷)", you can download these book. But allitebooks.com often updates, and the urls don't follow. Below is another way.

1. download the repo
    - you can download use the 'clone and download' button on the top right of this page.
    - you can also use git, if you like it. For example, if you are also using your pi, whitch has installed `git`, do as follows:
    ```bash
    cd ~
    git clone https://github.com/trevery/scrap-allitebooks.git
    cd ~/scrap-allitebooks/
    
    ```
2. I use python3 to execute this script.
   `python3 getUrl.py`
   By default, the getUrl.py will scrap the first 2 pages of allitebooks.com
   wait for a moment, and if everything is right, you will get 20 downling urls.
   
3. If you want to download more, you can edit the getUrl.py. 
   '''python
   	 pageNum = 2
	 subTitle = ''
   
   '''
   change the 'pageNum' for the numble you want to download. You can also change the subTitle, 
   for just downloading one specific sub theme. For example, you just wanna download the Hardware&DIY category,
   click the Hardware&DIY, you can get the subTitle from the url:http://www.allitebooks.com/hardware/
   modify
   
 
   ```python
   subTitle = 'hardware'
   
   ```
   
 4. enjoy it! Feel free to modified this script. hope you will share what you modified.
 and thanks to allitebooks.com. If you download too much e-books from this site, think about supporting this site.
