import time
from selenium import webdriver

# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()

# Navigate to the application home page
driver.get("DSA APP GOES HERE")

#Testing DSA Template Data

# AboutYou Page
# First Name
search_field = driver.find_element_by_id("firstName")
search_field.clear()
search_field.send_keys("Bob")
time.sleep(1)
# Last Name
search_field = driver.find_element_by_id("lastName")
search_field.clear()
search_field.send_keys("McAdoo")
time.sleep(1)
# DOB
search_field = driver.find_element_by_id("dateOfBirth")
search_field.clear()
search_field.send_keys("04/26/1997")
time.sleep(1)
# Street Address
search_field = driver.find_element_by_id("aboutMeAddress")
search_field.clear()
search_field.send_keys("226 Main St")
time.sleep(1)
# About You - Click Next
search_field = driver.find_element_by_id("about-you-next-button")
search_field.click()
time.sleep(1)
# popup confirmation
# Once finished with Aboutyou page, a pop up window is appearing with saved profiles.
# This dismisses that
button = driver.find_element_by_id("modal_btn_icon")
button.click()
time.sleep(1)

# STOPS WORKING HERE

# Add a Driver Button
search_field = driver.find_element_by_xpath('//div[contains(@class,"marg-top-625") ' 'and text()="' + 'Add Vehicle' + '"]').click()
search_field.click()
time.sleep(1)

# Confirm added driver
search_field = driver.find_element_by_class_name("vehicles-next-button")
search_field.click()


