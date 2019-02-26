""" Your Vehicles Page Subscript
    
"""
from datagen import vehicle as v
from datagen import general as g

HEADER = ["NumOfVehicles", "VehicleType", "VehicleVin", "VehicleOwnership",
            "VehicleRegistered", "VehicleUsage"]
#TODO Determine method of handling multiple vehicles


def makeList():
    """ Returns the randomly generated fields in the "Your Vehicle" page,
        according to the DSA template
    """
    #As per the initial test case 1 driver 1 vehicle
    vehiclenum = 1
    return [vehiclenum, v.randtype(), v.randVIN() , v.randownership(),
            g.yesno_question(), v.randusage()]