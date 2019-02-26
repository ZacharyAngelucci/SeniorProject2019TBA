import random
import sys
import datagen.person
import datagen.address

""" About You Page Subscript
Contains:
State, FirstName, MiddleName, LastName, Address,
Apartment, DateOfBirth, Email, Phone """

#Missing: FirstName, LastName, Apartment, Email
def makeList():
    state = datagen.address.randstate()
    FirstName = "CCSUFN" + state
    LastName = "CCSULN" + state
    Apartment = random.randint(1, 9999)
    Email = "plautomation@thehartford.com"
    aboutYouList = [state, FirstName, datagen.person.randMI(), LastName, datagen.address.randaddress(), Apartment, datagen.person.randDOB(), Email, datagen.person.randphonenum()]
    return aboutYouList



