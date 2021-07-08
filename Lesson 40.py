# Parsing HTML with the Beautiful Soup Module

import bs4, requests

res = requests.get('https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2505460.m570.l1313&_nkw=automate+the+boring+stuff&_sacat=0')

res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")

elems = soup.select('#srp-river-results > ul > li:nth-child(2) > div > div.s-item__info.clearfix > div.s-item__details.clearfix > div:nth-child(1) > span')

elems[0].text.strip() # strip getts rid of white space 
