import time
import csv
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By

# Read from CSV file
# Currently using sample test data from testData.csv
with open('testData.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        firstName = row[0]
        lastName = row[1]
        dob = row[2]
        address = row[3]

# create a new Firefox/Chrome session
driver = webdriver.Firefox()
# driver = webdriver.Chrome()
driver.implicitly_wait(30)

# Navigate to the application home page
driver.get("DSA APP Goes Here")

# Testing DSA Template Data

# ABOUT YOU PAGE
# First Name
driver.find_element_by_id("firstName").send_keys(firstName)

# Last Name
driver.find_element_by_id("lastName").send_keys(lastName)

# DOB
driver.find_element_by_id("dateOfBirth").send_keys(dob)

# Street Address
driver.find_element_by_id("aboutMeAddress").send_keys(address)

# About You - Click Next
driver.find_element_by_id("about-you-next-button").click()
time.sleep(1)

# popup confirmation
# This dismisses a pop up window appears with saved profiles.
driver.find_element_by_id("modal_btn_icon").click()
time.sleep(5)


# DRIVER PAGE
# Add a Driver Button
buttonclick = driver.find_element_by_class_name('add-vehicle-label')
action = webdriver.common.action_chains.ActionChains(driver)
action.move_to_element_with_offset(buttonclick, 5, 5)
action.click()
action.perform()
time.sleep(1)

# Select Yes for Vehicle Identification Number
driver.find_element_by_id("vinQuestion_div_add_0").click()

# Enter VIN Number
driver.find_element_by_id("vehicleVin").send_keys("JTHBD182610032265")
time.sleep(1)  # Don't remove

# Press Add Vehicle
driver.find_element_by_class_name("primary-cta").click()

# Confirm added driver
driver.find_element_by_id("vehicles-next-button").click()

# Second Confirmation Pop up
search_field = driver.find_element_by_class_name("primary-cta").click()

# Select Paid for
driver.find_element_by_id("vehicleOwnership_1_div_1_0").click()

# Select yes for registration
driver.find_element_by_xpath("//*[@id='vehicleRegistered_1_div_1_0']").click()

# STOPS WORKING HERE
#buttonclick = driver.find_element_by_class_name('col-xs-12')
#action = webdriver.common.action_chains.ActionChains(driver)
#action.move_to_element_with_offset(buttonclick, 10, 10)
#action.click()
#action.perform()
#selecto = driver.find_element_by_xpath("//ul[@id='dropdownId']//li[. = 'Commute to work/school']")
#selecto.click()

image = driver.find_element_by_id("col-xs-12 dropup")
driver.execute_script("arguments[0].value = 'col-xs-12 dropup open';", image)

#driver.close()