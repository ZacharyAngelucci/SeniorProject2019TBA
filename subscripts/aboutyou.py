import random
import sys
sys.path.insert(0, '../datagen')

from address import *
from person import *
import string

""" About You Page Subscript
Contains:
State, FirstName, MiddleName, LastName, Address,
Apartment, DateOfBirth, Email, Phone """

#Missing: FirstName, LastName, Apartment, Email
def makeList():
	state = randstate()
	FirstName = "CCSUFN" + state
	LastName = "CCSULN" + state
	Apartment = random.randint(1, 9999)
	Email = "plautomation@thehartford.com"
	aboutYouList = [state, FirstName, randMI(), LastName, randaddress(), Apartment, randDOB(), Email, randphonenum()]
	return aboutYouList

List = makeList();
for x in range (len(List)):
		print (List[x],)