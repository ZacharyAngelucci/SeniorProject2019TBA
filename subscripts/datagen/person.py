import random
import string
import calendar
from datetime import date, timedelta

def randMI(chance=0.8):
    """Returns a middle initial as a random letter from the alphabet
    Args:
        chance (float): Chance for having a middle name [0->0.999...]
            Defaults to 0.8
    """
    #should I keep this function?  How do we determine the chance of having no
    # middle initial?  set a default chance and let the function caller decide?
    if random.random() <= chance:
        return random.choice(string.ascii_uppercase)
    else:
        return ""

def randDOB(minage=55, maxage=120):
    """Returns a random Date Of Birth in the format of ddmmyyyy
    Args:
        minage (int): Minimum age in years the date of birth can be
            Defaults to 55 (AARP valid age)
        maxage (int): Maximum age in years the date of birth can be
            Defaults to 120 (oldest living person currently)
    """
    curdate = date.today()
    if calendar.isleap(curdate.year) and (curdate.month == 2 and curdate.day == 29):
        curdate = curdate + timedelta(days=1)
    mindate = curdate.replace(year=(curdate.year - minage))
    randdays = random.randint(0, (maxage - minage) * 365)
    #note the above calculation does not account for the extra day in leap years
    randdelta = timedelta(days=randdays)
    return "{0.month:02d}{0.day:02d}{0.year:4d}".format(mindate - randdelta)

def randphonenum():
    """Returns a random phone number following the North American Numbering Plan
    NPA-NXX-XXXX
        NPA = area code
        NXX-XXXX = subscriber number
            where N cannot equal 0 or 1
    """
    #valid area codes for USA
    NPA_code = [201, 202, 203, 205, 206, 207, 208, 209, 210, 212, 213, 214, 215,
                216, 217, 218, 219, 220, 224, 225, 228, 229, 231, 234, 239, 240,
                248, 251, 252, 253, 254, 256, 260, 262, 267, 269, 270, 272, 276,
                281, 301, 302, 303, 304, 305, 307, 308, 309, 310, 312, 313, 314,
                315, 316, 317, 318, 319, 320, 321, 323, 325, 330, 331, 332, 334,
                336, 337, 339, 340, 346, 347, 351, 352, 360, 361, 364, 380, 385,
                386, 401, 402, 404, 405, 406, 407, 408, 409, 410, 412, 413, 414,
                415, 417, 419, 423, 424, 425, 430, 432, 434, 435, 440, 442, 443,
                458, 463, 469, 470, 475, 478, 479, 480, 484, 501, 502, 503, 504,
                505, 507, 508, 509, 510, 512, 513, 515, 516, 517, 518, 520, 530,
                531, 534, 539, 540, 541, 551, 559, 561, 562, 563, 567, 570, 571,
                573, 574, 575, 580, 585, 586, 601, 602, 603, 605, 606, 607, 608,
                609, 610, 612, 614, 615, 616, 617, 618, 619, 620, 623, 626, 628,
                629, 630, 631, 636, 641, 646, 650, 651, 657, 660, 661, 662, 667,
                669, 670, 671, 678, 680, 681, 682, 684, 701, 702, 703, 704, 706,
                707, 708, 712, 713, 714, 715, 716, 717, 718, 719, 720, 724, 725,
                727, 731, 732, 734, 737, 740, 743, 747, 754, 757, 760, 762, 763,
                765, 769, 770, 772, 773, 774, 775, 779, 781, 785, 786, 787, 801,
                802, 803, 804, 805, 806, 808, 810, 812, 813, 814, 815, 816, 817,
                818, 828, 830, 831, 832, 843, 845, 847, 848, 850, 854, 856, 857,
                858, 859, 860, 862, 863, 864, 865, 870, 872, 878, 901, 903, 904,
                906, 907, 908, 909, 910, 912, 913, 914, 915, 916, 917, 918, 919,
                920, 925, 928, 929, 930, 931, 934, 936, 937, 938, 939, 940, 941,
                947, 949, 951, 952, 954, 956, 959, 970, 971, 972, 973, 978, 979,
                980, 984, 985, 989]
    subnum = str(random.randint(2, 9)) + "{:06d}".format(random.randint(0, 999999))
    subnumf = subnum[:3] + "-" + subnum[3:]
    return str(random.choice(NPA_code)) + "-" + subnumf