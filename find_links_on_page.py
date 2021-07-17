import requests
import re

# get url
url = input("Enter a URL (include 'https://'): ")

website = requests.get(url)
html = website.txt

# grab all links on page
links = re.findall('"((http|ftp)s?://.*?)"', html)

# output links
for link in links:
	print(link[0])
