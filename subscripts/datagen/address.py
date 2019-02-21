import random
import string

def randaddress():
    """Returns a random address in the following format
    [Street, city/town, 2 letter state, Zip code]
    """
    #TODO
    # Might be hard to generate each component individually is there a way to
    # pull a random address from somewhere?
    # https://openaddresses.io/
    # https://pe.usps.com/text/pub28/welcome.htm
    state = randstate()
    #TODO - Create a way to get a random city
    city = "ToDo"
    street = randstreet()
    zip = "{0:05d}".format(randzip())
    return [street, city, state, zip]

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
    size = 8
    chars = string.ascii_lowercase
    return ''.join(random.choice(chars) for _ in range(size))
    #TODO
    # How should we generate street names?

def randzip():
    #TODO
    # Over 42,000 zip codes in the US, I don't see an easy way of pulling from a
    # list of valid codes.  Might be easier to generate
    #TODO
    # Need to add fail cases for zip codes
    """Returns a random zipcode"""
    location = random.choice(open('ZipCodes.csv').readlines())
    return(location)

print(randaddress())