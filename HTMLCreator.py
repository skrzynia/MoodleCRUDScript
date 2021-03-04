import os



def createHTML(num, code):

	os.chdir(f"index\\lectures\\wk{num}")
	file = open(f"index{num}.html","w+")
	file.write(code)
	file.close()


def deleteHTML(num):
	os.chdir(f"index\\lectures\\wk{num}")
	if os.path.exists(f"index{num}.html"):
		os.remove(f"index{num}.html")
	else:
		print("The file does not exist")


def createDir(num):
	os.chdir('index\\lectures')
	print(os.getcwd())
	if os.path.exists(f"wk{num}"):
		arr = os.listdir()
		for a in arr:
			os.remove(a)
	else:
		try:
			os.mkdir(f"wk{num}")
			return ;
		except:
			print("Creation folder failed")
		else:
			print("Successfully created the folder")
		finally:
			return;


def isExisting(num):
	return True if os.path.exists(f"index\\lectures\\wk{num}") else False

def getHTMLTag(num):
	return f"<a href=index\\lectures\\wk{num}\\index{num}.html>Week {num} slides!</a>"