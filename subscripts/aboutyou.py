""" About You Page Subscript
"""
import random

from datagen import addressgen, persongen

HEADER = ["State", "FirstName", "MiddleName", "LastName", "Address", "Apartment",
          "DateOfBirth", "Email", "Phone Number"]


def makeList(validcase, state='all'):
    """	Returns the randomly generated fields in the "About You" page, according
            to the DSA template
    """
    address = addressgen.randaddress(state)  # [street, city, state, zip code, unit]
    address_body = address[:2]
    address_body.append(address[2] + "," + address[3])
    address_body_str = ", ".join(map(str, address_body))
    state = address[2]
    email = "plautomation@thehartford.com"
    DOB = persongen.randDOB()
    firstname = state + "CCSUFN"
    lastname = state + "CCSULN"
    if validcase == False:
        choice = random.randint(1, 4)
        if choice == 1:
                firstname = state + "CCSUFN" + str(random.randint(1,101))
        if choice == 2:
                lastname = state + "CCSULN" + str(random.randint(1,101))
        if choice == 3:
                chance = 0.5
                if random.random() <= chance:
                        DOB = "07202000" #Younger than 55
                else:
                        DOB = "07201800" #Older than 98
    
    return [state, firstname, persongen.randMI(), lastname, address_body_str,
            address[4].replace('\n',''), DOB, email, persongen.randphonenum()]