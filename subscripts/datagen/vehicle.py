import random
import string


def vehicletype():
    """Returns a random type of vehicle"""

    cartype = ["CAR", "SUV", "VAN", "PICKUP"]
    return random.choice(cartype)



def vehiclevin():
    """Returns a random 17 digit VIN"""
    size = 17
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(size))
    #TODO
    #Need to generate VIN relistically based on these factors
    #1 = Country of Origin
    #2 = Manufacturer
    #3 = Vehicle Type when combined with first two digits
    #4-9 = Vehicle descriptor(model, body type, etc)
    #10 = Letter indicating model year
    #11-17 = Production sequence numbers

def vehicleusage():
    """Returns a random vehicle use"""
    vehicleuse = ["Pleasure", "Commute", "Farming", "Business"]
    return random.choice(vehicleuse)


