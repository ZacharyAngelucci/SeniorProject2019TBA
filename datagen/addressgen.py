def randaddress():
    """Returns a random address in the following format
    [Street, city/town, 2 letter state, Zip code]
    """
    # https://openaddresses.io/ to get valid addresses
    # ['Street Number', 'Street', 'City', 'Zipcode', 'state']
    """Returns a random location consisting of a zip code, state and city
        format
            ['Street Number', 'Street', 'City', 'Zipcode', 'state']
        example.)
            ['25', 'Hayes Rd', 'East Hampton', '06424', 'CT']
    """
    location = random.choice(open('datagen\\AddressFile.csv').readlines())
    location_list = location.split(',')
    #['Street Number', 'Street', 'City', 'Zipcode', 'state']
    # [Street, city/town, 2 letter state, Zip code]
    location_list[3] = "{0:05d}".format(
        int(location_list[3]))  # format to 5 digit form
    # remove new line char
    location_list[4] = location_list[4][:2]
    return [location_list[0] + " " + location_list[1], location_list[2], location_list[4], location_list[3]]


def randzip():
    """Returns a 5 digit random zipcode from a file of valid zip codes"""
    zipcode = random.choice(
        open('subscripts\\datagen\\ZipCodes.csv').readlines())
    return "{0:05d}".format(int(zipcode))


def randstate():
    """Returns a random state in abbreviated form"""
    states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
              "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
              "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
              "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
              "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    return random.choice(states)


for i in range(3):
    print(randaddress())