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
    itera = -1
    state = None
    veh = -1
    drive = -1

    if r == 0:
        itera = config_data['Iterations']
    else:
        itera = r
    if s == None:
        state = config_data['State']
    else:
        state = s
    if v == 0:
        veh = config_data['Vehicals']
    else:
        veh = v
    if d == 0:
        drive = config_data['Drivers']
    else:
        drive = d

    if o == "CVS" or config_data['Output'] == "CSV":
        with open('Output.csv', 'w', newline='') as csvFile:
            data_writer = csv.writer(csvFile, dialect='excel')
            data_writer.writerow(make_header(1, 1))
            for i in range(itera):
                output = aboutyou.makeList() + yourvehicles.makeList() + yourdrivers.makeList()
                test_id = "TC" + "{0:03}".format(i + 1) + "-E2E-WEB-1V1D-" + output[0]
                list.insert(output, 0, test_id)
                data_writer.writerow(output)
    else:
        output = None
        for i in range(itera):
            output = aboutyou.makeList() + yourvehicles.makeList() + yourdrivers.makeList()
            test_id = "TC" + "{0:03}".format(i + 1) + "-E2E-WEB-1V1D-" + output[0]
            list.insert(output, 0, test_id)
        json.dump(output, 'Output.json')


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


main(iterations, state, vehicles, drivers, data_out)
