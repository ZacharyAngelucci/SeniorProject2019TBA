""" About You Page Subscript
"""
import random

from datagen import addressgen, persongen

HEADER = ["State", "FirstName", "MiddleName", "LastName", "Address", "Apartment",
          "DateOfBirth", "Email", "Phone Number"]


def makeList():
    """	Returns the randomly generated fields in the "About You" page, according
            to the DSA template
    """
    address = addressgen.randaddress(
    )  # [Street, city/town, 2 letter state, Zip code]
    state = address[2]
    firstname = state + "CCSUFN"
    lastname = state + "CCSULN"
    # Apartment is optional, currently apartment info from openaddress.io
    #   consists of more than just number addresses.
    apartment = ''
    email = "plautomation@thehartford.com"
    return [state, firstname, persongen.randMI(), lastname, ", ".join(map(str, address)),
            apartment, persongen.randDOB(), email, persongen.randphonenum()]
