from DSAWebTest import start, readCSV, webTest

mode = start()
dataArray = readCSV()
webTest(dataArray, mode)