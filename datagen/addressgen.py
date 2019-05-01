import random
import string
import os


def randaddress(state='all'):
    """Returns a random address in the following format
    [Street, city/town, 2 letter state, Zip code]
    Addresses are picked from a 1000 sample
    Addresses sourced from https://openaddresses.io/
    Picks a random spot based on the file size, move to the next line and return
    that line
    address header = NUMBER,STREET,CITY,STATE,POSTCODE,UNIT
    """
    filename = 'datagen\\sampleaddresses\\'
    buffer_EOF = 100
    file_size = os.stat(filename)[6]

    if state == 'all':
        state = randstate()
    filename = filename + state + '.csv'
    file = open(filename, 'r')
    # buffer in bytes, should be longer than the longest address line
    file.seek(random.randint(0, file_size-buffer_EOF), 0)
    # skip to next complete line
    file.readline()
    line = file.readline()
    #print("Current Line:\t" + str(line))
    address_parts = line.split(',')
    #print("Split Line:\t " + str(address_parts))
    # format zipcode to 5 digit
    try:
        address_parts[4] = "{0:05d}".format(int(address_parts[4]))
    except ValueError as identifier:
        print(identifier)
        print("Value Error:\t-" + " ".join(address_parts))
    except:
        print("unknown error")
    
    # remove new line char
    address_parts[5] = address_parts[5][:2]
    # Return as [street num + street, city, state, zip code, unit] format
    return [address_parts[0] + " " + address_parts[1], address_parts[2], address_parts[3], address_parts[4], address_parts[5]]


def randzip():
    """Returns a 5 digit random zipcode from a file of valid zip codes"""
    zipcode = random.choice(
        open('subscripts\\datagen\\ZipCodes.csv').readlines())
    return "{0:05d}".format(int(zipcode))


def randstate():
    """Returns a random state in abbreviated form"""
    states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
              'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
              'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
              'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
              'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI']
    #no sample data for WY yet
    return random.choice(states)
