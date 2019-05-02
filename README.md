# SeniorProject 2019 - Team TBA
## Test Data Generation for the Digital Sales Application
Purpose of this project is to generate test data used for automated testing

## Prerequisites

Python 3 and pyYAML are required to run the main project

Command to install pyYAML
```
pip install PyYAML
```

## Getting Started

To use this project run the master.py file. You can either run the file itself through your IDE or from the command line.  This master file accepts several arguments.
- i # of iterations
- s 'ab' two letter state or ALL
- v # of vehicles
- d # of drivers
- o 'output type' (CSV or JSON)

If an argument is not specified on the command line, then the value is derived from the config file. All arguments are optional and can be requested in any order.

Usage
``` 
    master.py -i # -s 'ab' -v # -d # -o 'CSV or JSON'
```
Example
```
    py master.py -i 100 -s CT -v 1 -d 1 -o CSV
```

## First Time Run

If no config file is present, then running master.py will create a default config file.

## Configuration Details

Config settings can be set in the command line however, they can be saved in the config.yaml file for easier usage.
- Iterations: # of iterations
- State: 'ab' two letter state or ALL
- Vehicles: # of vehicles
- Drivers: # of drivers
- Output: 'output type' (CSV or JSON)

## Output
Outputted test data will be in the file Output.csv in project root directory. The filename will be Output with the file extension of the selected output type. 
This will overwrite any previous output

ex.) Output.csv or Output.json

### File Structure
    .
    ├── datagen                     # Categorized random data generator
    ├── subscripts                  # Scripts for each page of data
    ├── tools                       # testing and data generation setup modules
    ├── master.py
    ├── config.yaml
    └── README.md

# Tools
## DSAWebTest
Python program to test the generated data from the main program. It uses the CSV output file from master.py and individual tests every row in "Output.csv". If an individual test fails due to problems like timeouts, fail data, or incorrect data than the program will terminate the test and move on to testing the next row. The DSAWebTest also creates a report file called "testReport.csv" with the results of the test, a failed test is labeled as failed and lists the error info.

## Prerequisites
```
Firefox GeckoDriver

Selenium WebDriver
```
## How to Install

### Selenium
```
pip install selenium
```
### GeckoDriver

Download:
https://github.com/mozilla/geckodriver/releases

Add the location of "geckdriver.exe" to path by
```
Control Panel --> Large Icons --> System Settings --> Advanced Systems Settings --> Environment Variables --> Select Path in System Variables --> Edit --> Add the location of "geckodriver"
```
## Modes

### Demo Mode:
 Runs the test visually by showing the testing being done on the browser in real time. 

### Test Mode: 
Runs the test in Firefox headless mode which hides any visual browsers and indicates each finished or failed test in the console.

## Running the program
Before you use this program make sure you run "master.py" with the "csv" flag and check that "Output.csv" exists in the project folder. Run "DSAWebTestMain.py" and you will be prompted with an option to choose Test Mode and Demo mode by typing "demo" or "test".

## OpenAddresses-US-Parser
Python program to format USA state addresses from USA region datasets taken from openaddress.io. Where the dataset from openaddress.io is split up between either state or city files this program combs through the statewide files (if present).  If no useable data is found in the state file, then it will then search through each city file.  The result is a csv file for each of the 50 states with the following header.  
```
    'NUMBER', 'STREET', 'CITY', 'POSTCODE', 'UNIT'
```

### Prerequisites

#### Dependencies
Python 3 and pandas are required to run this tool

Command to install pandas
```
pip install pandas
```
### Input
Download US region data from openaddress.io and unzip the contents in the Input folder, be sure to give each region its own folder.

ex.) .\\Input\\openaddr-collected-us_midwest\\...

### Input File Structure
    .
    .
    .
    ├── tools           # Modules for formatting data
    .   ├── dataformatter           # Modules for formatting data
    .   ├── Input                   # US region data from open address.io
    .   |       └── Regiondata 1
        |       └── Regiondata ...
        |       └── Regiondata n
        ├── Output                  # CSV file per state
        |       └── Sample          # Sample selection and final filtered CSV files per state
        ├── main.py
        ├── sample.py
        └── README.md

## Running the Program

To use this tool, make sure you have downloaded the region data and placed it in the Input folder.  Run the main.py file to compile all state address data in the Output folder.  Run the sample.py file to select x sample addresses from each state, apply the final filter and out put the remaining valid data entries in the sample folder.  By default, the sample.py takes a sample of 1000 addresses from each state csv file.


