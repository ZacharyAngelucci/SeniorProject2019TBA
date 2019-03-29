import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# create a new Firefox session
driver = webdriver.Chrome()
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

# Last Name
search_field = driver.find_element_by_id("lastName")
search_field.clear()
search_field.send_keys("McAdoo")

# DOB
search_field = driver.find_element_by_id("dateOfBirth")
search_field.clear()
search_field.send_keys("04/26/1997")

# Street Address
search_field = driver.find_element_by_id("aboutMeAddress")
search_field.clear()
search_field.send_keys("226 Main St")

# About You - Click Next
nextbutton = driver.find_element_by_id("about-you-next-button")
nextbutton.click()
time.sleep(1)
# popup confirmation
# Once finished with Aboutyou page, a pop up window is appearing with saved profiles.
# This dismisses that
button = driver.find_element_by_id("modal_btn_icon")
button.click()
time.sleep(5)

# Add a Driver Button
buttonclick = driver.find_element_by_class_name('add-vehicle-label')
action = webdriver.common.action_chains.ActionChains(driver)
action.move_to_element_with_offset(buttonclick, 5, 5)
action.click()
action.perform()
time.sleep(1)

# Select Yes for Vehicle Identification Number

search_field = driver.find_element_by_id("vinQuestion_div_add_0")
search_field.click()


# Enter VIN Number
search_field = driver.find_element_by_id("vehicleVin")
search_field.clear()
search_field.send_keys("JTHBD182610032265")
time.sleep(1)

# Press Add Vehicle
nextbutton = driver.find_element_by_class_name("primary-cta")
nextbutton.click()
time.sleep(1)

# Confirm added driver
nextbutton = driver.find_element_by_id("vehicles-next-button")
nextbutton.click()

# Second Confirmation Pop up
search_field = driver.find_element_by_class_name("primary-cta")
search_field.click()
time.sleep(1)

# Select Paid for
search_field = driver.find_element_by_id("vehicleOwnership_1_div_1_0")
search_field.click()

# Select yes for registration
driver.find_element_by_xpath("//*[@id='vehicleRegistered_1_div_1_0']").click()

# STOPS WORKING HERE

# Select vehicle use drop down menu
buttonclick = driver.find_element_by_id('vehicleRegistered_1_div_1_1')
action = webdriver.common.action_chains.ActionChains(driver)
action.move_to_element_with_offset(buttonclick, 5, 5)
action.click()
action.perform()

