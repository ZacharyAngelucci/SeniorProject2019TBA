import random
import time
import string

def randgender():
    """Returns a random gender"""
    gender = ["Male", "Female"]
    return random.choice(gender)

def employmentstatus():
    """Returns a random employment status"""
    estatus = ["Employed", "Unemployed"]
    return random.choice(estatus)
    # TODO
    # Find out the rest of the drop down coices
def maritalstatus():
    """Returns a random marital status"""
    mstatus = ["Single", "Married", "Divorced"]
    return random.choice(mstatus)
    # TODO
    # Find out the rest of the drop down coices
def currentresidence():
    """Returns a random residence type"""
    rstatus = ["I own my home", "Apartment"]
    return random.choice(rstatus)
    # TODO
    # Find out the rest of the drop down coices
def currentlyinsured():
    """Returns a random insurance status"""
    istatus = ["Yes, with your own policy", "No"]
    return random.choice(istatus)
    # TODO
    # Find out the rest of the drop down coices
def coveragerange():
    """Return random coverage range"""
    range = ["$100,000/$300,000"]
    return random.choice(range)
    #TODO
    #Find out the rest of the drop down coices

def strTimeProp(start, end, format, prop):
    """Calculates a random date in between two points in time"""
    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(format, time.localtime(ptime))

def policyexpiration():
    """Return a policy expiration date between two dates
        Typically they are 6 months long"""
    return strTimeProp("3/1/2019", "9/1/2019", '%m/%d/%Y', random.random())

def policyterm():
    """Return a policy term length"""
    term = ["6 Months", "1 Year"]
    return random.choice(term)
    #TODO
    #We need to change the random genration of policy expiration date based on how long the policy term is

def ssn():
    #TODO
    #Its impossible to generate valid ssn

#print(policyterm())
#print(randgender(), policyexpiration(), coveragerange(), employmentstatus(), maritalstatus(), currentresidence(), currentlyinsured())