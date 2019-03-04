import random
import time
import string

def randgender():
    """Returns a random gender"""
    gender = ["Male", "Female"]
    return random.choice(gender)

def maritalstatus():
    """Returns a random marital status"""
    mstatus = ["Single (never married)", "Married", "Domestic Partner", "Widowed", "Legally Separated", "Divorced"]
    return random.choice(mstatus)

def employmentstatus():
    """Returns a random employment status"""
    estatus = ["Self Employed", "Employed", "Unemployed", "Homemaker", "Retired", "Disabled", "Student"]
    return random.choice(estatus)

def currentresidence():
    """Returns a random residence type"""
    rstatus = ["I own my home", "I own my condo", "Rental", "Mobile/Motorhome", "Other"]
    return random.choice(rstatus)

def currentlyinsured():
    """Returns a random insurance status"""
    istatus = ["Yes, with your own policy", "Yes, on your parent's policy", "Yes, your employer insures your car", 
    "No, your insurance ran out less than a month ago", "No, your insurance ran out more than a month ago", 
    "No, due to your military deployment/overseas", "Never needed insurance until now"]
    return random.choice(istatus)

def coveragerange():
    """Return random coverage range"""
    crange = ["$10,000 / $20,000", "$15,000 / $30,000", "$20,000 / $40,000", "$25,000 / $50,000", "$30,000 / $60,000",
    "$35,000 / $80,000", "$50,000 / $100,000", "$100,000 / $300,000", "$250,000 / $500,000", "$500,000 / $500,000 or greater",
    "single limits less than $25,000", "single limits between $25,000 - $50,000", "single limits between $50,001 - $100,000",
    "single limits between $100,001 / $300,000", "single limits between $100,001 / $300,000", "single limits greater than $300,000", "Unknown"]
    return random.choice(crange)

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
    term = ["6 months", "12 months"]
    return random.choice(term)
    #TODO
    #We need to change the random genration of policy expiration date based on how long the policy term is

def ssn():
    #TODO
    #Its impossible to generate valid ssn

#print(policyterm())
#print(randgender(), policyexpiration(), coveragerange(), employmentstatus(), maritalstatus(), currentresidence(), currentlyinsured())