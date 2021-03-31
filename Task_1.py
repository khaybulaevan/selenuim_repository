
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('http://www.google.com/')

elem = browser.find_element_by_name('q')
elem.send_keys("Selenium" + Keys.RETURN)

browser.quit()