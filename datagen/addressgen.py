import random
import string
import os

def randaddress():
    """Returns a random address in the following format
    [Street, city/town, 2 letter state, Zip code]
    """
    #TODO
    # Might be hard to generate each component individually is there a way to
    # pull a random address from somewhere?
    # https://openaddresses.io/
    # https://pe.usps.com/text/pub28/welcome.htm
    location = randlocation() # ['zipcode', 'City', 'state']
    # should it return it as a list or string?
    return [randstreet(), location[1], location[2], location[0]]

def randstate():
    """Returns a random state in abbreviated form"""
    states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
                "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
                "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
                "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
                "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    return random.choice(states)

def randstreet():
    """Returns a random street name and number"""
    #TODO
    # Find a way to generate valid street names
    size = 8
    chars = string.ascii_lowercase
    return ''.join(random.choice(chars) for _ in range(size))
    

def randzip():
    """Returns a 5 digit random zipcode from a file of valid zip codes"""
    #TODO
    # Need to add fail cases for zip codes
    
    # Use the below to check your current directory.  For my environment open would
    # look in the home directory of the project and not this files directory
    # cwd = os.getcwd()
    # print(cwd)
    zipcode = random.choice(open('subscripts\\datagen\\ZipCodes.csv').readlines())
    return "{0:05d}".format(int(zipcode))

#alternate function to a random matching zip, city, and state
def randlocation():
    """Returns a random location consisting of a zip code, state and city
        format
            ['Street Number', 'Street', 'City', 'Zipcode', 'state']
        example.)
            ['25', 'Hayes Rd', 'East Hampton', '06424', 'CT']
    """
    location = random.choice(open('datagen\AddressFile.csv').readlines())
    loca_list = location.split(',')
    loca_list[3] = "{0:05d}".format(int(loca_list[3]))  # format to 5 digit form
    loca_list[4] = loca_list[4][:2]                     # remove new line char
    return loca_list
    
for i in range(100):
    randlocation()