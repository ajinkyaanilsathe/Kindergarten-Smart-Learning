import requests
#import wget
from zipfile import ZipFile
import os
import time
import shutil

def fixImageNow():

	if os.path.exists("images/images.zip"):
		os.remove("images/images.zip")
	
	# conn = sqlite3.connect(r'database/smartdata.db')
	# c = conn.cursor()
	# sql = "SELECT alphabet from words"

	# c.execute(sql)

	# result = c.fetchall()

	# print(result)
	alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	for x in alpha:
		get = os.getcwd()
		location = "images"
		path = os.path.join(get,location,x)
		print("path - ",path)
		if(os.path.isdir(path)):
			print("yes exist")
			shutil.rmtree(path)

	print("-------")
			
	url = 'https://srv-file9.gofile.io/download/WpIUCi/images.zip' #https://gofile.io/d/WpIUCi
	r = requests.get(url)
	with open("images/images.zip", "wb") as code:
		code.write(r.content)
	
	file_name = "images/images.zip"
	with ZipFile(file_name, 'r') as zip:
		zip.printdir()
		zip.extractall('images/')

#fixImageNow()