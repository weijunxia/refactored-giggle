# Downloading from the Web with Request Module

import requests

res = requests.get('http://automatetheboringstuff.com/files/rj.txt')

# .raise_for_status() returns nothing if request worked
# .status_code returns '200' if it worked
# write-binary mode open(filename, 'wb')
# request mod is a 3rd party mod for downloading web pages and files
# requests.get() returns a Response object
# raise_for_status() response method will raise an exception if the download faield
# you can save a downloaded file to your hard drive with calls to the iter_content() method

# playFile = open('RomeoAndJuliet.txt', 'wb')
# >>> import os
# >>> os.getcwd()
# '/Users/weijunxia/Documents'
# >>> os.chdir('python')
# >>> os.getcwd()
# '/Users/weijunxia/Documents/python'
# >>> playFile = open('RomeoAndJuliet.txt', 'wb')
# >>> for chunk in res.iter_content(100000): # this section writes the rj.txt file with the requested page
	# playFile.write(chunk)

# 100000
# 78978
# >>> playFile.close()
