from selenium import webdriver
import time
import os
import json

def printToPdf(num,url):
	path = os.getcwd()
	appState = {
		"recentDestinations": [
			{
				"id": "Save as PDF",
				"origin": "local",
				"account": ""
			}
		],
		"selectedDestinationId": "Save as PDF",
		"version": 2
	}

	profile = {'printing.print_preview_sticky_settings.appState': json.dumps(appState),
	           'savefile.default_directory': path+f'\\index\\lectures\\wk{num}'}

	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_experimental_option('prefs', profile)
	chrome_options.add_argument('--kiosk-printing')

	driver = webdriver.Chrome(options=chrome_options)
	driver.get(manageURL(url))
	time.sleep(5)
	driver.execute_script('window.print();')
	time.sleep(5)
	driver.quit()



def manageURL(url):
	new_url = ""
	for i in url:

		if ord(i) == 35:
			new_url += ("?print-pdf")
			new_url += (i)
		else:
			new_url +=(i)

	return new_url





