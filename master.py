import os.path
import csv
import sys

from subscripts import aboutyou, yourdrivers, yourvehicles, configgen

iterations = sys.argv[1]
state = sys.argv[2]
vehicles = sys.argv[3]
drivers = sys.argv[4]

def main(i, s, v, d):
    config_data = configgen.config()

    with open('Output.csv', 'w', newline='') as csvFile:
        data_writer = csv.writer(csvFile, dialect='excel')
        data_writer.writerow(make_header(1, 1))
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


def export(out, format):
    return


main(iterations, state, vehicles, drivers)
