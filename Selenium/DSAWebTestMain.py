import os
from selenium.common.exceptions import TimeoutException
from DSAWebTest import start, readCSV, webTest

file = open("testReport.txt", "w") 

# Clears terminal
os.system("clear")

# Set Start Mode
mode = start()

# Read CSV File into 2D Array
dataArray = readCSV()
 

# Test Data From CSV File
length = len(dataArray[0])
for x in range(length):
    try:
        webTest(dataArray, mode, x)
    except Exception as e:
        if 'Unable to locate element' in str(e):
            file.write("Failed") 
            continue
file.close() 