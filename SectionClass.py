from WebScrapper import getTitle, getHTML

class SectionClass:
	title = ''
	slideHTML = ''
	videoURL = ''


	def __init__(self,slideURL):
		self.slideURL = slideURL
		self.title = getTitle(self.slideURL)
		self.slideHTML = getHTML(self.slideURL)



	def __str__(self):
		return f"""This SectionClass contains {self.title} as Title,
				{self.slideHTML} as HTML and {self.videoURL} as video	
		
		
		"""


print(SectionClass("https://mikhail-cct.github.io/ooapp2/wk4/#/"))