import time
import csv
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options

print("Starting DSA App Test...")
testReport = open("testReport.txt","w+")
testReport.write("Test Report -")
# Read from CSV file
# Currently using sample test data from testData.csv
from selenium.webdriver.support.wait import WebDriverWait
with open('testData.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        firstName = row[2]
        lastName = row[4]
        dob = row[7]
        address = row[5]
        vin = row[12]
        vOwnership = row[13]
        vResgistered = row[14]
        vUsage = row[15]
        gender = row[18]
        marital = row[20]
        employment = row[19]
        residence = row[21]
        lastFive = row[22]
        accident = row[23]
        defence = row[24]
        smallBusiness = row[25]
        currInsured = row[26]
        bodyCoverage = row[27]
        polExpiry = row[28]
        polterm = row[29]
        lineCount = row[30]
        print(lineCount+" - CSV File Found...")
        testReport.write("Test #" + lineCount)
        # splits address into individual fields
        address = address.split(',')
        streetAd = address[0]
        zipCode = address[3][1:]

        print("Opening Headless Web Driver...")
        options = Options()
        options.headless = True
        driver = webdriver.Firefox(options=options)
        driver.implicitly_wait(30)
        print ("Headless Firefox Initialized")
        # Navigate to the application home page
        driver.get("https://qa-quote.thehartford.com/sales/landing-page?zip="+zipCode+"&PLCode=002121&organic=true&affinity=AARP&lob=Auto")
        print("Launching DSA App...")

        # ABOUT YOU PAGE
        # DOB
        driver.find_element_by_id("dateOfBirth").send_keys(dob)

        # First Name
        driver.find_element_by_id("firstName").send_keys(firstName)

        # Last Name
        driver.find_element_by_id("lastName").send_keys(lastName)

        # Street Address
        driver.find_element_by_id("aboutMeAddress").send_keys(streetAd)

        # About You - Click Next
        driver.find_element_by_id("about-you-next-button").click()


        # popup confirmation
        # This dismisses a pop up window appears with saved profiles.

        driver.find_element_by_id("modal_btn_icon").click()

        print("About You Finished...")
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
        driver.find_element_by_id("vehicleVin").send_keys(vin)
        time.sleep(1)  # Don't remove

        # Press Add Vehicle
        driver.find_element_by_class_name("primary-cta").click()

        # Confirm added driver
        driver.find_element_by_id("vehicles-next-button").click()
        print("Added Driver...")
        # Second Confirmation Pop up
        search_field = driver.find_element_by_class_name("primary-cta").click()

        # Select Paid for
        if vOwnership == "Paid For":
            driver.find_element_by_id("vehicleOwnership_1_div_1_0").click()
        elif vOwnership == "Financed":
            driver.find_element_by_id("vehicleOwnership_1_div_1_1").click()
        else:
            driver.find_element_by_id("vehicleOwnership_1_div_1_2").click()

        # Select yes for registration
        if vResgistered == "yes":
            driver.find_element_by_xpath("//*[@id='vehicleRegistered_1_div_1_0']").click()
        else:
            driver.find_element_by_xpath("//*[@id='vehicleRegistered_1_div_1_1']").click()

        # Vehicle Usage Drop Down
        dropDown = driver.find_element_by_xpath("//a[@id='vehicleUsage_1' and contains(.,'"+vUsage+"')]")
        driver.execute_script("arguments[0].click();",dropDown)

        # Press Save Vehicle
        driver.find_element_by_id("desktopSaveButton_1").click()
        time.sleep(6)

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
        time.sleep(8)
        print("Vehicles Page Finished...")
        # Your Drivers
        # Select Male or Female
        if gender == "Male":
            driver.find_element_by_id("gender_div_0_0").click()
        else:
            driver.find_element_by_id("gender_div_0_1").click()

        # Select Marital Status
        dropDown = driver.find_element_by_xpath("//a[@id='maritalStatus' and contains(.,'"+marital+"')]")
        driver.execute_script("arguments[0].click();",dropDown)

        # Select Employment Status
        dropDown = driver.find_element_by_xpath("//a[@id='employmentStatus' and contains(.,'"+employment+"')]")
        driver.execute_script("arguments[0].click();",dropDown)

        # Select Residence
        dropDown = driver.find_element_by_xpath("//a[@id='primaryResidence' and contains(.,'"+residence+"')]")
        driver.execute_script("arguments[0].click();",dropDown)

        # Yes/No Have you lived there for at least 5 years
        if lastFive == "Yes":
            driver.find_element_by_id("livedFiveYears_div_0_0").click()
        else:
            driver.find_element_by_id("livedFiveYears_div_0_1").click()

        # Have you been licensed for at least 3 years?
        dropDown = driver.find_element_by_xpath("//a[@id='licensedDuration' and contains(.,'Less than 1 year')]")
        driver.execute_script("arguments[0].click();",dropDown)
        time.sleep(5)
        #driver.find_element_by_id("icon icon-close").click()

        # During the past 5 years, have you had an accident (regardless of fault), violation or claim?
        if accident == "Yes":
            driver.find_element_by_id("violation_div_0_0").click()
        else:
            driver.find_element_by_id("violation_div_0_1").click()


        # Have you maintained a B (or better) grade point average and/or part of the top 20% of your class?
        # driver.find_element_by_id("goodStudent_div_0_1").click()

        # Have you taken a Defensive Driving course in the past 3 years?
        if defence == "Yes":
            driver.find_element_by_id("defensiveDriving_div_0_0").click()
        else:
            driver.find_element_by_id("defensiveDriving_div_0_1").click()

        # Do you or your listed drivers own or work for a small business?
        if defence == "Yes":
            driver.find_element_by_id("ownSmallBusiness_div_0_0").click()
        else:
            driver.find_element_by_id("ownSmallBusiness_div_0_1").click()

        # Press Save Driver Button
        driver.find_element_by_id("saveButton_0").click()
        time.sleep(10)# wait for loading screen to go away
        print("Driver Saved...")
        # Are you an AARP member
        driver.find_element_by_id("aarpMembership_div_aarp_1").click()

        # Next button
        driver.find_element_by_id("drivers-next-button").click()

        # Not adding your spouse/domestic partner
        if marital == "Married":
            dropDown = driver.find_element_by_xpath("//a[@id='spouse' and contains(.,'Permanently living outside the household for more than 1 year')]")
            driver.execute_script("arguments[0].click();",dropDown)
            driver.find_element_by_xpath("//*[@class='btn btn-primary']").click()

        # Are you currently insured?
        dropDown = driver.find_element_by_xpath("//a[@id='currentInsurance' and contains(.,'"+currInsured+"')]")
        driver.execute_script("arguments[0].click();",dropDown)
        time.sleep(2)

        # What is your current range of bodily injury coverage? If you're unsure, take your best guess
        dropDown = driver.find_element_by_xpath("//a[@id='currentBodilyInjuryRange' and contains(.,'"+bodyCoverage+"')]")
        driver.execute_script("arguments[0].click();",dropDown)
        time.sleep(2)

        # When will your current policy expire?
        driver.find_element_by_id("dateField").send_keys(polExpiry)

        # How long have you been with your current carrier?
        dropDown = driver.find_element_by_xpath("//a[@id='yearsCurrentInsurance' and contains(.,'1 year')]")
        driver.execute_script("arguments[0].click();",dropDown)
        time.sleep(2)

        # Is your policy 6 or 12 months long?
        if polterm == "6 months":
            driver.find_element_by_id("currentTermDurationPeriod_div__0").click()
        else:
            driver.find_element_by_id("currentTermDurationPeriod_div__1").click()

        # Click "Choose Your Coverages"
        driver.find_element_by_id("current-insurance-next-button").click()
        time.sleep(5)
        print(lineCount+" - Test Complete!")
        testReport.write(" - Success\n")
        # Click next on popup
        #driver.find_element_by_xpath("btn btn-primary btn-lg btn-block").click()

testReport.close()
driver.close()