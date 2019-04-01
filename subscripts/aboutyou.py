""" About You Page Subscript
"""
import random

from datagen import addressgen, persongen

HEADER = ["State", "FirstName", "MiddleName", "LastName", "Address", "Apartment",
          "DateOfBirth", "Email", "Phone Number"]


def makeList(state='all'):
    """	Returns the randomly generated fields in the "About You" page, according
            to the DSA template
    """
    address = addressgen.randaddress(state)  # [street, city, state, zip code, unit]
    address_body = address[:2]
    address_body.append(address[2] + " " + address[3])
    address_body_str = ", ".join(map(str, address_body))
    state = address[2]
    firstname = state + "CCSUFN"
    lastname = state + "CCSULN"
    email = "plautomation@thehartford.com"
    return [state, firstname, persongen.randMI(), lastname, address_body_str,
            address[4], persongen.randDOB(), email, persongen.randphonenum()]