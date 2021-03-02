from requests import get,post
import bs4
from requests import get

def getHTML(url):
	request = get(url)
	return request.text



def getTitle(url):
	request = get(url)
	soup = bs4.BeautifulSoup(request.text,'html.parser')
	return soup.title.string

def getVideo():
	request = get("https://drive.google.com/drive/folders/1pFHUrmpLv9gEJsvJYKxMdISuQuQsd_qX")
	soup = bs4.BeautifulSoup(request.text, 'html.parser')
	print(soup.prettify())



