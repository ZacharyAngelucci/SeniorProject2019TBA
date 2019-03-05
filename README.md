# SeniorProject2019TBA
Purpose of this project is to generate test data used for automated testing

## Prerequisites

Python 3 and pyYAML are required to run this project

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
    ├── subscripts                  # Scirpts for each page of data
    ├── datagen                     # Categorized random data generator modules
    ├── master.py
    ├── config.yaml
    └── README.md