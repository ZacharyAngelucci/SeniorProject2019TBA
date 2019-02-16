import random

def randaddress():
    """Returns a random address in the following format
    [Street, city/town, 2 letter state, Zip code]
    """
    #TODO 
    # Might be hard to generate each component individually is there a way to
    # pull a random address from somewhere?
    # https://openaddresses.io/
    # https://pe.usps.com/text/pub28/welcome.htm
    pass

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
    street = str(random.randrange(0,9999))
    #TODO 
    # How should we generate street names?

    return street

def randzip():
    """Returns a random zipcode"""
    #TODO
    # Over 42,000 zip codes in the US, I don't see an easy way of pulling from a 
    # list of valid codes.  Might be easier to generate 
    pass