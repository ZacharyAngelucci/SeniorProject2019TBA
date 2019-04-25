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
    try:
        webTest(dataArray, mode, x)
    except Exception as e:
        os.system("pkill -f firefox")
        if 'Unable to locate element' in str(e):
            file.write("Failed") 
            print(e)

            continue
        else:
            print(e)
file.close()