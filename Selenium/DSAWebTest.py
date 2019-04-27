import time
import csv
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def start():
    # Choose Run Mode
    modeSelection = input("Choose Test/Demo Mode\n")
    if modeSelection == "demo":
        modeSelection = False
    else:
        modeSelection = True
    return modeSelection

def readCSV():
    count = 1
    listOfRows = []
    firstName = []
    lastName = []
    dob = []
    address = []
    vin = []
    vOwnership = []
    vResgistered = []
    vUsage = []
    gender = []
    marital = []
    employment = []
    residence = []
    lastFive = []
    accident = []
    defence = []
    smallBusiness = []
    currInsured = []
    bodyCoverage = []
    polExpiry = []
    polterm = []
    lineCount = []
    # Read from CSV file
    # Currently using sample test data from testData.csv
    with open(os.path.join( os.getcwd(), '..', 'Output.csv' )) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            firstName.append(row[2])
            lastName.append(row[4])
            dob.append(row[7])
            address.append(row[5])
            vin.append(row[12])
            vOwnership.append(row[13])
            vResgistered.append(row[14])
            vUsage.append(row[15])
            gender.append(row[18])
            marital.append(row[20])
            employment.append(row[19])
            residence.append(row[21])
            lastFive.append(row[22])
            accident.append(row[23])
            defence.append(row[24])
            smallBusiness.append(row[25])
            currInsured.append(row[26])
            bodyCoverage.append(row[27])
            polExpiry.append(row[28])
            polterm.append(row[29])
            lineCount.append(count)
            count += 1
    # Create an array of arrays    
    listOfRows.append(firstName)
    listOfRows.append(lastName)
    listOfRows.append(dob)
    listOfRows.append(address)
    listOfRows.append(vin)
    listOfRows.append(vOwnership)
    listOfRows.append(vResgistered)
    listOfRows.append(vUsage)
    listOfRows.append(gender)
    listOfRows.append(marital)
    listOfRows.append(employment)
    listOfRows.append(residence)
    listOfRows.append(lastFive)
    listOfRows.append(accident)
    listOfRows.append(defence)
    listOfRows.append(smallBusiness)
    listOfRows.append(currInsured)
    listOfRows.append(bodyCoverage)
    listOfRows.append(polExpiry)
    listOfRows.append(polterm)
    listOfRows.append(lineCount)
    return listOfRows


def webTest(array, modeSelection, n):
    """Executes Website Test with parameters asking for array of data and test mode"""
    print("Opening Headless Web Driver...")
    options = Options()
    options.headless = modeSelection
    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(40)
    print ("Headless Firefox Initialized")
    # Navigate to the application home page
    driver.set_window_size(1920, 1080)
    # splits address into individual fields
    address = array[3][n].split(',')
    streetAd = address[0]
    state = address[2]
    zipCode = address[3]
    driver.get("https://qa-quote.thehartford.com/sales/landing-page?zip="+zipCode+"&PLCode=002121&organic=true&affinity=AARP&lob=Auto")
    time.sleep(5)
    # ABOUT YOU PAGE
    # DOB
    driver.find_element_by_id("dateOfBirth").send_keys(array[2][n])

    # First Name
    driver.find_element_by_id("firstName").send_keys(array[0][n])

    # Last Name
    driver.find_element_by_id("lastName").send_keys(array[1][n])

    # Street Address
    driver.find_element_by_id("aboutMeAddress").send_keys(streetAd)

    # VT special button
    if (state == " VT"):
        driver.find_element_by_id("vtTerms_div_add_0").click()

    # About You - Click Next
    driver.find_element_by_id("about-you-next-button").click()
    time.sleep(1)
    
    # popup confirmation
    # This dismisses a pop up window appears with saved profiles.
    try:
        driver.find_element_by_id("modal_btn_icon").click()
    except Exception as e:
        print(e)

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
    driver.find_element_by_id("vehicleVin").send_keys(array[4][n])
    time.sleep(1)  # Don't remove

    # Press Add Vehicle
    driver.find_element_by_class_name("primary-cta").click()
    time.sleep(1)

    # Confirm added driver
    driver.find_element_by_id("vehicles-next-button").click()
    # Second Confirmation Pop up
    search_field = driver.find_element_by_class_name("primary-cta").click()

    # Select Paid for
    if array[5][n] == "Paid For":
        driver.find_element_by_id("vehicleOwnership_1_div_1_0").click()
    elif array[5][n] == "Financed":
        driver.find_element_by_id("vehicleOwnership_1_div_1_1").click()
    else:
        driver.find_element_by_id("vehicleOwnership_1_div_1_2").click()

    # Select yes for registration
    if array[6][n] == "yes":
        driver.find_element_by_xpath("//*[@id='vehicleRegistered_1_div_1_0']").click()
    else:
        driver.find_element_by_xpath("//*[@id='vehicleRegistered_1_div_1_1']").click()

    # MA specific questions
    if (state == " MA"):
        driver.find_element_by_id("riskStateVehilceRegisteredInd_div_maRiskStateVehilceRegisteredInd_0").click()
        driver.find_element_by_id("garagingAddress_1_div_1_0").click()

    # Vehicle Usage Drop Down
    dropDown = driver.find_element_by_xpath("//a[@id='vehicleUsage_1' and contains(.,'"+array[7][n]+"')]")
    driver.execute_script("arguments[0].click();",dropDown)

    # Press Save Vehicle
    driver.find_element_by_id("desktopSaveButton_1").click()
    time.sleep(8)

    # Press Select your Drivers
    driver.find_element_by_id("vehicles-next-button").click()
    time.sleep(9)

    # Press Add Driver Details
    driver.find_element_by_id("drivers-next-button").click()
    time.sleep(2)

    # Select Yes For Confirm your Drivers
    driver.find_element_by_id("allDriversListed_div__0").click()

    # Press Continue Button on Confirm your Drivers
    driver.find_element_by_xpath("//*[@class='btn btn-primary']").click()
    time.sleep(8)
    # Your Drivers
    # Select Male or Female
    if array[8][n] == "Male":
        driver.find_element_by_id("gender_div_0_0").click()
    else:
        driver.find_element_by_id("gender_div_0_1").click()

    # Select Marital Status
    dropDown = driver.find_element_by_xpath("//a[@id='maritalStatus' and contains(.,'"+array[9][n]+"')]")
    driver.execute_script("arguments[0].click();",dropDown)

    # Select Employment Status
    dropDown = driver.find_element_by_xpath("//a[@id='employmentStatus' and contains(.,'"+array[10][n]+"')]")
    driver.execute_script("arguments[0].click();",dropDown)

    # Select Residence
    dropDown = driver.find_element_by_xpath("//a[@id='primaryResidence' and contains(.,'"+array[11][n]+"')]")
    driver.execute_script("arguments[0].click();",dropDown)

    # Yes/No Have you lived there for at least 5 years
    if array[12][n] == "Yes":
        driver.find_element_by_id("livedFiveYears_div_0_0").click()
    else:
        driver.find_element_by_id("livedFiveYears_div_0_1").click()

    # Have you been licensed for at least 3 years?
    dropDown = driver.find_element_by_xpath("//a[@id='licensedDuration' and contains(.,'Less than 1 year')]")
    driver.execute_script("arguments[0].click();",dropDown)
    time.sleep(5)

    # During the past 5 years, have you had an accident (regardless of fault), violation or claim?
    if array[13][n] == "Yes":
        driver.find_element_by_id("violation_div_0_0").click()
    else:
        driver.find_element_by_id("violation_div_0_1").click()


    # Have you maintained a B (or better) grade point average and/or part of the top 20% of your class?
    # driver.find_element_by_id("goodStudent_div_0_1").click()

    # Have you taken a Defensive Driving course in the past 3 years?
    if array[14][n] == "Yes":
        driver.find_element_by_id("defensiveDriving_div_0_0").click()
    else:
        driver.find_element_by_id("defensiveDriving_div_0_1").click()

    # Do you or your listed drivers own or work for a small business?
    if array[15][n] == "Yes":
        driver.find_element_by_id("ownSmallBusiness_div_0_0").click()
    else:
        driver.find_element_by_id("ownSmallBusiness_div_0_1").click()

    # Press Save Driver Button
    driver.find_element_by_id("saveButton_0").click()
    time.sleep(14)# wait for loading screen to go away
    # Are you an AARP member
    driver.find_element_by_id("aarpMembership_div_aarp_1").click()

    # Next button
    driver.find_element_by_id("drivers-next-button").click()

    # Not adding your spouse/domestic partner
    if array[9][n] == "Married" or "Domestic Partner":
        dropDown = driver.find_element_by_xpath("//a[@id='spouse' and contains(.,'Permanently living outside the household for more than 1 year')]")
        driver.execute_script("arguments[0].click();",dropDown)
        driver.find_element_by_xpath("//*[@class='btn btn-primary']").click()

    # Are you currently insured?
    dropDown = driver.find_element_by_xpath("//a[@id='currentInsurance' and contains(.,'"+array[16][n]+"')]")
    driver.execute_script("arguments[0].click();",dropDown)
    time.sleep(2)

    # What is your current range of bodily injury coverage? If you're unsure, take your best guess
    dropDown = driver.find_element_by_xpath("//a[@id='currentBodilyInjuryRange' and contains(.,'"+array[17][n]+"')]")
    driver.execute_script("arguments[0].click();",dropDown)
    time.sleep(2)

    # When will your current policy expire?
    driver.find_element_by_id("dateField").send_keys(array[18][n])

    # How long have you been with your current carrier?
    dropDown = driver.find_element_by_xpath("//a[@id='yearsCurrentInsurance' and contains(.,'1 year')]")
    driver.execute_script("arguments[0].click();",dropDown)
    time.sleep(4)

    # Is your policy 6 or 12 months long?
    if array[19][n] == "6 months":
        driver.find_element_by_id("currentTermDurationPeriod_div__0").click()
    else:
        driver.find_element_by_id("currentTermDurationPeriod_div__1").click()

    # Click "Choose Your Coverages"
    driver.find_element_by_id("current-insurance-next-button").click()
    time.sleep(5)
    # Click next on popup
    #driver.find_element_by_xpath("btn btn-primary btn-lg btn-block").click()
    print("FINISHED")
    driver.close()

