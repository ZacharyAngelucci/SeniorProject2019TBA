import random
import string


def randtype():
    """Returns a random type of vehicle"""

    cartype = ["CAR", "SUV", "VAN", "PICKUP"]
    return random.choice(cartype)

def randVIN():
    """Returns a random 17 digit VIN from a list of 6 valid VINs"""
    vin = ["JTHBD182610032265", "JNKAY41E23M002732", "2HGES267X4H566590", "YV1RH59H342419180", "1G8ZJ5576PZ244260", "1FALP6535SK248174"]
    return random.choice(vin)


def randownership():
    """returns a randome vehicle ownership value"""
    ownership = ["Paid For", "Financed", "Leased"]
    return random.choice(ownership)

def randusage():
    """Returns a random vehicle use"""
    usage = ["Pleasure", "Commute", "Farming", "Business"]
    return random.choice(usage)


