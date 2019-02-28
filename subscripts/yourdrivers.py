""" Your Drivers Page Subscript
"""
from datagen import general

HEADER = ['NumberOfDrivers', 'DriverAdded', 'DriverGender1', 'DriverEmploymentStatus1',
          'DriverMaritalStatus1', 'CurrentResident1', 'LivedLast5Years1', 'AnyAccidents1',
          'DefensiveDriving', 'OwnSmallBusiness', 'Current Insurance Details', 'Bodily Injury Liability',
          'CurrentPolicyExpiry', 'Policy Term', 'SSN']

def makeList():
    numDrivers = 1
    driverAdded = general.yesno_question()
    livedLast5Years = general.yesno_question()
    accidents = general.yesno_question()
    defensiveDriving = general.yesno_question()
    ownSmallBusiness = general.yesno_question()

    return [numDrivers, driverAdded, livedLast5Years, accidents, defensiveDriving, ownSmallBusiness]
