import os
from selenium.common.exceptions import TimeoutException
from DSAWebTest import start, readCSV, webTest

file = open("testReport.txt", "w") 
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
    try:
        webTest(dataArray, mode, x)
        file.write(","+str(dataArray[3][x])+",")
        file.write("Success\n") 
    except Exception as e:
        os.system("taskkill /IM firefox.exe /F")
        file.write(","+str(dataArray[3][x])+ ",Failed,")
        file.write(str(e)+"\n")
        continue

file.close() 