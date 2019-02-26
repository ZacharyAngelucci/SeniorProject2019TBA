""" About You Page Subscript
"""
import random
import string

from datagen import address as a
from datagen import person as p

HEADER = ["FirstName","MiddleName","LastName","Address","Apartment",
			"DateOfBirth", "Email", "Phone Number"]

def makeList():
	"""	Returns the randomly generated fields in the "About You" page, according
		to the DSA template
	"""
	address = a.randaddress() # ['street', zipcode', 'City', 'state']
	state = address[3]
	firstname = state + "CCSUFN"
	lastname = state + "CCSULN"
	#Does everyone need an apartment number?
	apartment = random.randint(0, 9999)
	email = "plautomation@thehartford.com"
	return [state, firstname, p.randMI(), lastname, ", ".join(map(str, address)),
			apartment, p.randDOB(), email, p.randphonenum()]

#print(makeList())