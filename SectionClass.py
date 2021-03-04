from WebScrapper import getTitleAndHTML, getVideo


class SectionClass:
	title = ''
	slideHTML = ''
	videoURL = ''


	def __init__(self,week,slideURL, date):
		self.slideURL = slideURL
		self.date = date
		self.week = week
		self.title, self.slideHTML = getTitleAndHTML(self.slideURL)
		self.videoURL = getVideo(self.date)


	def __str__(self):
		return f"""This SectionClass contains {self.title} as Title,
				{self.slideHTML} as HTML and {self.videoURL} as video	
		
		
		"""


