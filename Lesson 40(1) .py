import bs4, requests

def getEbayPrice(productURL):
    res = requests.get(productURL)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#srp-river-results > ul > li:nth-child(2) > div > div.s-item__info.clearfix > div.s-item__details.clearfix > div:nth-child(1) > span')
    return elems[0].text.strip()
    

price = getEbayPrice('https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2505460.m570.l1313&_nkw=automate+the+boring+stuff&_sacat=0')
print('The price is ' + price)

# web pages are plaintext files formatted as HTML
# HTML can be parsed with the BeautifulSoup module
# BeautifulSoup is imported with the name bs4
# Pass the string with the HTML to the bs4.BeautifulSoup() function to get a Soup object
# The Soup object has a select() method that can be passed a string of the CSS selector for an HTML tag.
# You can get a CSS selector string from the broser's developer tools by right-clicking the element and selecting Copy CSS Path.
# The select() nethod will return a list of matching Elements objects.
