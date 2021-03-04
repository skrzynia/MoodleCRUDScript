import os
from WebScrapper import getTitleAndHTML


def createHTML(num, code):

	filename = f"index\\lectures\\wk{num}\\index{num}.html"
	os.makedirs(os.path.dirname(filename),exist_ok=True)
	with open(filename,"w") as f:
		f.write(code)


def deleteHTML(num):
	os.chdir(f"index\\lectures\\wk{num}")
	if os.path.exists(f"index{num}.html"):
		os.remove(f"index{num}.html")
	else:
		print("The file does not exist")



def getHTMLTag(num):
	return f"<a href=https://github.com/skrzynia/MoodleCRUDScript/blob/master/index/lectures/wk1/index1.html>Week {num} slides!</a><br><br>"