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

To use this project run the master.py file. Alter run settings in the config.yaml file.  Outputed test data will be in the file Output.csv in project root directory 

## First Time Run

If no config file is present, then running master.py will create a default config file.

## Configuration Details

The config file is used to modify the test data generated
Current configurations
- Iterations: #
    - The number of test data lines produced

Future configurations
- Drivers
    - Number of drivers per test case
- Vehicles
    - Number of Vehicles per test case
- Output type
    - File type test data is outputted
    - Currently csv, will add json and nosql in future

### File Structure
    .
    ├── datagen                     # Categorized random data generator
    ├── subscripts                  # Scripts for each page of data
    ├── tools                       # testing and data generation setup modules
    ├── master.py
    ├── config.yaml
    └── README.md

# Tools
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

