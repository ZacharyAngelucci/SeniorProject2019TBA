import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://qa-quote.thehartford.com/sales/landing-page?zip=06088&PLCode=002121&organic=true&affinity=AARP&lob=Auto')

#First Name
search = browser.find_element_by_id('firstName')
search.send_keys("Bob")
#Last Name
search = browser.find_element_by_id('lastName')
search.send_keys("Dole")
#Street Address
search = browser.find_element_by_id('aboutMeAddress')
search.send_keys("10 N Main St")
#Apt/Suite
search = browser.find_element_by_id('aboutMeAddressPostFix')
search.send_keys("30")
#City
search = browser.find_element_by_id('noFoundCity')
search.send_keys("New York")
#State
search = browser.find_element_by_id('noFoundState')
search.send_keys("NY")
#ZIPCODE
search = browser.find_element_by_id('noFoundZipCodeInput')
search.send_keys("11201")
#DOB
search = browser.find_element_by_id('dateOfBirth')
search.send_keys("04/26/1997")
search.send_keys(Keys.RETURN) # hit return after you enter search text

