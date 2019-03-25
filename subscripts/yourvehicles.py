""" Your Vehicles Page Subscript
"""
from datagen import vehiclegen
from datagen import general as g

HEADER = ["NumOfVehicles", "VehicleType", "VehicleVin", "VehicleOwnership",
          "VehicleRegistered", "VehicleUsage"]


def makeList():
    """ Returns the randomly generated fields in the "Your Vehicle" page,
        according to the DSA template
    """
    # As per the initial test case 1 driver 1 vehicle
    vehiclenum = 1
    return [vehiclenum, vehiclegen.randtype(), vehiclegen.randVIN(), vehiclegen.randownership(),
            g.yesno_question(), vehiclegen.randusage()]
