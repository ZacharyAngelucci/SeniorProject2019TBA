""" About You Page Subscript
Contains:
State, FirstName, MiddleName, LastName, Address,
Apartment, DateOfBirth, Email, Phone """
import random
import string

from datagen import address as a
from datagen import person as p

def makeList():
	"""
	TODO add docstring
	"""
	state = a.randstate()
	firstname = state + "CCSUFN"
	lastname = state + "CCSULN"
	apartment = random.randint(0, 9999)
	email = "plautomation@thehartford.com"
	return [state, firstname, p.randMI(), lastname, a.randaddress(), apartment, p.randDOB(), email, p.randphonenum()]