import os.path
import csv
import sys
import json

from subscripts import aboutyou, yourdrivers, yourvehicles, configgen

iterations = int(sys.argv[1], 10)
state = sys.argv[4]
vehicles = int(sys.argv[2], 10)
drivers = int(sys.argv[3], 10)
data_out = sys.argv[5]


def main(r, s, v, d, o):
    config_data = configgen.config()

    with open('Output.csv', 'w', newline='') as csvFile:
        data_writer = csv.writer(csvFile, dialect='excel')
        data_writer.writerow(make_header(1, 1))
        if r != 0:
            for i in range(r):
                output = aboutyou.makeList() + yourvehicles.makeList() + yourdrivers.makeList()
                test_id = "TC" + "{0:03}".format(i + 1) + "-E2E-WEB-1V1D-" + output[0]
                list.insert(output, 0, test_id)
                data_writer.writerow(output)
        else:
            for i in range(config_data['Iterations']):
                output = aboutyou.makeList() + yourvehicles.makeList() + yourdrivers.makeList()
                test_id = "TC" + "{0:03}".format(i + 1) + "-E2E-WEB-1V1D-" + output[0]
                list.insert(output, 0, test_id)
                data_writer.writerow(output)


def make_header(v, d):
    header = ["Test Case"] + aboutyou.HEADER
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


def export(out, f):
    if f == "json":
        json.dump(out, 'Output.json')
    else:
        if os.path.isfile('Output.csv'):
            with open('Output.csv', 'w', newline='') as csvFile:
                data_writer = csv.writer(csvFile, dialect='excel')
                data_writer.writerow(out)
        else:
            with open('Output.csv', 'w', newline='') as csvFile:
                data_writer = csv.writer(csvFile, dialect='excel')
                data_writer.writerow(make_header(1, 1))
                data_writer.writerow(out)


main(iterations, state, vehicles, drivers, data_out)
