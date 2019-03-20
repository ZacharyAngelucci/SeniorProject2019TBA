import yaml
import os.path
import csv

from subscripts import aboutyou, yourdrivers, yourvehicles, configgen


def main():
    config_data = configgen.config()

    with open('Output.csv', 'w', newline='') as csvFile:
        data_writer = csv.writer(csvFile, dialect='excel')
        data_writer.writerow(make_header(1, 1))
        for i in range(config_data['Iterations']):
            output = aboutyou.makeList() + yourvehicles.makeList() + yourdrivers.makeList()
            test_id = "TC" + "{0:03}".format(i + 1) + "-E2E-WEB-1V1D-" + output[0]
            list.insert(output, 0, test_id)
            data_writer.writerow(output)


def make_header(vpages, dpages):
    header = ["Test Case"] + aboutyou.HEADER
    for i in range(1, vpages):
        temp = list(yourvehicles.HEADER.len() - 1)
        for j in range(1, yourvehicles.HEADER.len()):
            temp[j] = yourvehicles.HEADER[j] + i
    return header


def export(out):
    return
