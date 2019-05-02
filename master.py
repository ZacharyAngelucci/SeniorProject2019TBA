"""
Master file to run the test data generation program.
Can be run from either the command line or running the actual file itself.
Arguments:
    If an argument is not specified on the command line then the value is 
    derived from the config file.  All arguments are optional and can be 
    requested in any order.
        -i #iterations 
        -s 'ab'(two letter state) 
        -v #vehicles
        -d #drivers
        -o 'output type'(CSV or JSON)
Usage 
    master.py -i # -s 'ab' -v # -d # -o 'CSV or JSON'
Example
    $python master.py -i 100 -s CT -v 1 -d 1 -o CSV
Output
    Output will be in the root folder, filename will be Output with the
    chosen filetype so either Output.csv or Output.json
"""

import csv
import sys
import json
import argparse
import random

from subscripts import aboutyou, yourdrivers, yourvehicles, configgen

parser = argparse.ArgumentParser()


def main():
    parser.add_argument('-i', action='store', dest='arg_iterations',
                        help='[int] Number of cases to generate')
    parser.add_argument('-s', action='store', dest='arg_state',
                        help='[ab] Two letter state abbriviation state to pull addresses from')
    parser.add_argument('-v', action='store', dest='arg_vehicles',
                        help='[int] Number of vehicles per case')
    parser.add_argument('-d', action='store', dest='arg_drivers',
                        help='[int] Number of drivers per case')
    parser.add_argument('-o', action='store', dest='arg_output_type',
                        help='[CSV or JSON] Output file type for the test data')

    # command line arguments trump config settings
    # if not set result will be None
    results = parser.parse_args()
    iterations = results.arg_iterations
    state = results.arg_state
    vehicles = results.arg_vehicles
    drivers = results.arg_drivers
    output = results.arg_output_type

    # fill in empty args with config settings
    # parse non-None answers to preferred data type
    config_data = configgen.config()
    if iterations == None:
        iterations = config_data['Iterations']
    else:
        iterations = int(iterations)
    if state == None:
        state = config_data['State']
    else:
        state = state.upper()
    if vehicles == None:
        vehicles = config_data['Vehicles']
    else:
        vehicles = int(vehicles)
    if drivers == None:
        drivers = config_data['Drivers']
    else:
        drivers = int(drivers)
    if output == None:
        output = config_data['Output']
    else:
        output = output.upper()

    # set Test case identifier
    test_case_id = '-E2E-WEB-{}V{}D-'.format(vehicles, drivers)

    # Generate test data depending on file type
    if output == 'CSV':
        with open('Output.csv', 'w', newline='') as csvFile:
            data_writer = csv.writer(csvFile, dialect='excel')
            data_writer.writerow(make_header(1, 1))
            for i in range(iterations):
                # Determine if test case will be valid or not
                chance = 0.8
                if random.random() <= chance:
                    validcase = True
                else:
                    validcase = False
                row = aboutyou.makeList(
                    validcase, state=state) + yourvehicles.makeList() + yourdrivers.makeList()
                test_id = 'TC' + '{0:03}'.format(i + 1) + test_case_id + row[0]
                list.insert(row, 0, test_id)
                data_writer.writerow(row)
    else:
        output = None
        for i in range(iterations):
            row = aboutyou.makeList(
                validcase) + yourvehicles.makeList() + yourdrivers.makeList()
            test_id = 'TC' + '{0:03}'.format(i + 1) + '-E2E-WEB-1V1D-' + row[0]
            list.insert(row, 0, test_id)
        json.dump(output, 'Output.json')


def make_header(v, d):
    header = ['Test Case'] + aboutyou.HEADER
    if v != 0:
        temp = [yourvehicles.HEADER[0]]
        for i in range(0, v):
            for j in range(1, len(yourvehicles.HEADER)):
                temp.append(yourvehicles.HEADER[j] + str(i + 1))
            header.extend(temp)
    if d != 0:
        temp = [yourdrivers.HEADER[0]]
        for i in range(0, d):
            for j in range(1, len(yourdrivers.HEADER)):
                temp.append(yourdrivers.HEADER[j] + str(i + 1))
            header.extend(temp)
    return header

main()
