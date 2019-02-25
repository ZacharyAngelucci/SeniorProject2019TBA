import random

def polarquestion(chance=.5):
    """ Returns a yes or a no
    Args:
        chance (float): Chance for yes result [0->0.999...]
            Defaults to 0.5
    """
    if random.random() <= chance:
        return "Yes"
    else:
        return "No"