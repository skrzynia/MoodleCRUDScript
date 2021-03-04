from requests import get,post
import bs4
from requests import get
import re


def getTitleAndHTML(url):
	request = get(url)
	soup = bs4.BeautifulSoup(request.text,'html.parser')
	return (soup.title.string,request.text)

def getVideo(date):
	url = get("https://drive.google.com/drive/folders/1pFHUrmpLv9gEJsvJYKxMdISuQuQsd_qX")
	soup = bs4.BeautifulSoup(url.text, 'html.parser')
	videos = soup.find_all('div', class_='Q5txwe')
	arr = []
	for video in videos:
		video_id = video.parent.parent.parent.parent.attrs['data-id']
		video_name = video.attrs['data-tooltip']
		arr.append((video_name, video_id))

	for tup in arr:
		name, vid_id = tup
		x = re.search(f"{date}", name)
		if not x == None:
			video_tag = f'<iframe src="https://drive.google.com/file/d/{vid_id}/preview" width="640" height="480"></iframe><br><br>'
			return video_tag



