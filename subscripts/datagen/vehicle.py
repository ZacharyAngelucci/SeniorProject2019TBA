import random
import string


def randtype():
    """Returns a random type of vehicle"""

    cartype = ["CAR", "SUV", "VAN", "PICKUP"]
    return random.choice(cartype)

def randVIN():
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

def randownership():
    """returns a randome vehicle ownership value"""
    ownership = ["Paid For", "Financed", "Leased"]
    return random.choice(ownership)

def randusage():
    """Returns a random vehicle use"""
    usage = ["Pleasure", "Commute", "Farming", "Business"]
    return random.choice(usage)