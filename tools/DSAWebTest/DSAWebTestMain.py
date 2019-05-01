import os
from selenium.common.exceptions import TimeoutException
from DSAWebTest import start, readCSV, webTest

file = open("testReport.txt", "a") 
# Clears terminal
os.system('cls' if os.name == 'nt' else 'clear')

# Set Start Mode
mode = start()

# Read CSV File into 2D Array
dataArray = readCSV()
 
# Test Data From CSV File
length = len(dataArray[0])
for x in range(1,length):
    
    file.write(str(x))
    address = dataArray[3][x].split(',')
    state = address[2]
    try:
        webTest(dataArray, mode, x)
        file.write(","+state+",")
        file.write("Success\n") 
    except Exception as e:
        print("FAILED")
        os.system("taskkill /IM firefox.exe /F")
        file.write(","+state+",Failed,")
        file.write(str(e))
        continue

file.close() 