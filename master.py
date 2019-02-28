import yaml
import os.path
import csv

from subscripts import aboutyou, yourdrivers, yourvehicles

configData = {'Iterations': 0}
iterations = None
output = None
testID = None

if os.path.isfile("config.yaml"):
    with open('config.yaml') as f:
        configData = yaml.safe_load(f)
else:
    with open('config.yaml', 'w') as f:
        yaml.dump(configData, f, default_flow_style=False)
    quit()

with open('Output.csv', 'w', newline='') as csvFile:
    dataWriter = csv.writer(csvFile, dialect='excel')
    dataWriter.writerow(['Test Case', 'State', 'FirstName', 'MiddleName', 'LastName', 'Address', 'Apartment', 'DateOfBirth', 'Email', 'Phone', 'NumOfVehicles', 'VehicleType1', 'VehicleVin1', 'VehicleOwnverShip1', 'VehicleRegistered1', 'VehicleUsage1',	'NumberOfDrivers', 'DriverAdded', 'DriverGender1', 'DriverEmploymentStatus1', 'DriverMaritalStatus1', 'CurrentResident1', 'LivedLast5Years1', 'AnyAccidents1', 'DefensiveDriving', 'OwnSmallBusiness', 'Current Insurance Details',	'Bodily Injury Liability', 'CurrentPolicyExpiry', 'Policy Term', 'SSN'])
    for i in range(configData['Iterations']):
        output = aboutyou.makeList() + yourvehicles.makeList()
        testID = "TC" + "{0:03}".format(i + 1) + "-E2E-WEB-1V1D-" + output[0]
        list.insert(output, 0, testID)
        dataWriter.writerow(output)