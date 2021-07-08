# Controlling the Browser with the Selenium Module

from selenium import webdriver

browser = webdriver.Chrome()

# import selenium you need to run: 'from selenium import webdriver
# to open browser run: browser = webdriver.Chrome()
# to send the browser to a URL, run: browser.get('URL')
# browser.find_elements_by_css_selector() method will return a list of WebElement objects
# the click() method will click on an element in the browser
# the send_keys() method will type into a specific element in the browser
# the submit() method will simulate clicking on the Submit button for a form
# the browser can also be controlled with these methods: back(), forward(),
# refresh(), quit()
