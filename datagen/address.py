import random
import string

def randaddress():
    st = randstate();
    street = randstreet();
    zp = randzip();

def randstate():
    """Returns a random state in abbreviated form"""
    states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
                "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
                "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
                "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
                "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    return random.choice(states)

def randstreet(size=8, chars=string.ascii_lowercase):
    """Returns a random street name and number ("hviwen")"""
    return ''.join(random.choice(chars) for _ in range(size))

def randzip(size=5, chars=string.digits):
    """Returns a random zipcode ("85734")"""
    return ''.join(random.choice(chars) for _ in range(size))
    #TODO
    # Over 42,000 zip codes in the US, I don't see an easy way of pulling from a
    # list of valid codes.  Might be easier to generate
randaddress();
