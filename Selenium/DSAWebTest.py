import time
import csv
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By

# Read from CSV file
# Currently using sample test data from testData.csv
from selenium.webdriver.support.wait import WebDriverWait

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
# DOB
driver.find_element_by_id("dateOfBirth").send_keys(dob)

# First Name
driver.find_element_by_id("firstName").send_keys(firstName)

# Last Name
driver.find_element_by_id("lastName").send_keys(lastName)

# Street Address
driver.find_element_by_id("aboutMeAddress").send_keys(address)

# About You - Click Next
driver.find_element_by_id("about-you-next-button").click()
time.sleep(2)

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

# Vehicle Usage Drop Down

dropDown = driver.find_element_by_xpath("//a[@id='vehicleUsage_1' and contains(.,'Pleasure')]")
driver.execute_script("arguments[0].click();",dropDown)

# Press Save Vehicle
driver.find_element_by_id("desktopSaveButton_1").click()
time.sleep(4)

# Press Select your Drivers
driver.find_element_by_id("vehicles-next-button").click()
time.sleep(7)

# Press Add Driver Details
driver.find_element_by_id("drivers-next-button").click()
time.sleep(2)

# Select Yes For Confirm your Drivers
driver.find_element_by_id("allDriversListed_div__0").click()

# Press Continue Button on Confirm your Drivers
driver.find_element_by_xpath("//*[@class='btn btn-primary']").click()
time.sleep(2)
# Your Drivers
# Select Male or Female
driver.find_element_by_id("gender_div_0_0").click()

# Select Marital Status
dropDown = driver.find_element_by_xpath("//a[@id='maritalStatus' and contains(.,'Married')]")
driver.execute_script("arguments[0].click();",dropDown)

# Select Employment Status
dropDown = driver.find_element_by_xpath("//a[@id='employmentStatus' and contains(.,'Employed')]")
driver.execute_script("arguments[0].click();",dropDown)

# Select Residence
dropDown = driver.find_element_by_xpath("//a[@id='primaryResidence' and contains(.,'I own my home')]")
driver.execute_script("arguments[0].click();",dropDown)

# Yes/No Have you lived there for at least 5 years
driver.find_element_by_id("livedFiveYears_div_0_0").click()

# Have you been licensed for at least 3 years?
dropDown = driver.find_element_by_xpath("//a[@id='licensedDuration' and contains(.,'Less than 1 year')]")
driver.execute_script("arguments[0].click();",dropDown)
time.sleep(5)
#driver.find_element_by_id("icon icon-close").click()

# During the past 5 years, have you had an accident (regardless of fault), violation or claim?
driver.find_element_by_id("violation_div_0_1").click()

# Have you maintained a B (or better) grade point average and/or part of the top 20% of your class?
driver.find_element_by_id("goodStudent_div_0_1").click()

# Have you taken a Defensive Driving course in the past 3 years?
driver.find_element_by_id("defensiveDriving_div_0_1").click()

# Do you or your listed drivers own or work for a small business?
driver.find_element_by_id("ownSmallBusiness_div_0_1").click()

# Press Save Driver Button
driver.find_element_by_id("saveButton_0").click()
time.sleep(5)

# Are you an AARP member
driver.find_element_by_id("aarpMembership_div_aarp_1").click()

# Next button
driver.find_element_by_id("drivers-next-button").click()

# Not adding your spouse/domestic partner
dropDown = driver.find_element_by_xpath("//a[@id='spouse' and contains(.,'Permanently living outside the household for more than 1 year')]")
driver.execute_script("arguments[0].click();",dropDown)

# Click Continue on spouse pop up
driver.find_element_by_xpath("//*[@class='btn btn-primary']").click()

# Are you currently insured?
dropDown = driver.find_element_by_xpath("//a[@id='currentInsurance' and contains(.,'Yes, with your own policy')]")
driver.execute_script("arguments[0].click();",dropDown)
time.sleep(2)

# What is your current range of bodily injury coverage? If you're unsure, take your best guess
dropDown = driver.find_element_by_xpath("//a[@id='currentBodilyInjuryRange' and contains(.,'$20,000 / $40,000')]")
driver.execute_script("arguments[0].click();",dropDown)
time.sleep(2)

# When will your current policy expire?
driver.find_element_by_id("dateField").send_keys("06/06/2019")

# How long have you been with your current carrier?
dropDown = driver.find_element_by_xpath("//a[@id='yearsCurrentInsurance' and contains(.,'1 year')]")
driver.execute_script("arguments[0].click();",dropDown)
time.sleep(2)

# Is your policy 6 or 12 months long?
driver.find_element_by_id("currentTermDurationPeriod_div__0").click()
#driver.close()