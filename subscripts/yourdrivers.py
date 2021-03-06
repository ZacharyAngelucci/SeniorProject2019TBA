""" Your Drivers Page Subscript
"""
from datagen import general, drivergen


HEADER = ['NumberOfDrivers', 'DriverAdded', 'DriverGender1', 'DriverEmploymentStatus1',
          'DriverMaritalStatus1', 'CurrentResident1', 'LivedLast5Years1', 'AnyAccidents1',
          'DefensiveDriving', 'OwnSmallBusiness', 'Current Insurance Details', 'Bodily Injury Liability',
          'CurrentPolicyExpiry', 'Policy Term']


def makeList():
    numDrivers = 1
    driverAdded = general.yesno_question()
    drivergender1 = drivergen.randgender()
    driveremploymentstatus1 = drivergen.employmentstatus()
    drivermaritalstatus1 = drivergen.maritalstatus()
    currentresident1 = drivergen.currentresidence()
    livedLast5Years = general.yesno_question()
    #accidents = general.yesno_question()
    accidents = 'No'
    #defensiveDriving = general.yesno_question()
    defensiveDriving = 'No'
    ownSmallBusiness = general.yesno_question()
    currentinsurancedetails = drivergen.currentlyinsured()
    bodilyinjuryliability = drivergen.coveragerange()
    currentpolicyexpiry = drivergen.policyexpiration()
    policyterm = drivergen.policyterm()

    return [numDrivers, driverAdded, drivergender1, driveremploymentstatus1,
            drivermaritalstatus1, currentresident1, livedLast5Years, accidents,
            defensiveDriving, ownSmallBusiness, currentinsurancedetails,
            bodilyinjuryliability, currentpolicyexpiry, policyterm]
