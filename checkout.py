import payments
import random
from datetime import datetime, timedelta
import database
now = datetime.today().date()
# Function for generating room numbers
def room(nr):
    g = len(nr)
    x = ""
    for y in range(g):
        K = str(nr[y])
        x = x + "," + K
    return x

# Function for month input checking
def mnt():
    mn = int(input("ENTER MONTH:"))
    if mn > 12:
        print("INVALID")
        return mnt()
    elif mn < 1:
        print("INVALID")
        return mnt()
    else:
        return mn

# Function for year input checking
def yer():
    r = int(input("ENTER YEAR:"))
    if r < 2024:
        print("INVALID")
        return yer()
    elif r > 2025:
        print("INVALID")
        return yer()
    else:
        return r

# Function for date input checking
def dat():
    d = int(input("ENTER DATE:"))
    if d > 31:
        print("INVALID")
        return dat()
    elif d < 1:
        print("INVALID")
        return dat()
    else:
        return d

# Function for generating ID
def ids():
    return random.randint(1000, 9999)

# Function for generating room numbers
def RN():
    li = []
    n = int(input("ENTER NO OF ROOMS:"))
    for x in range(n):
        i = random.randrange(100, 400, 10)
        li.append(i)
    return li, n

# Function for phone number checking
def phn():
    ph = input("ENTER MOBILE NO(10 digits)::")
    l = len(ph)
    if l == 10:
        return ph
    else:
        print("INVALID MOBILE NUMBER::10 DIGITS")
        return phn()

# Function for aadhar number checking
def add():
    pad = input("ENTER AADHAR NO(12 digits)::")
    l = len(pad)
    if l == 12:
        return pad
    else:
        print("INVALID AADHAR NUMBER::12 DIGITS")
        return add()

# Function for date checking
def tme(f):
    tday = datetime.today().date()
    print()
    print("FOR DATE OF CHECK IN::")
    year = yer()
    month = mnt()
    day = dat()
    date1 = datetime(year, month, day).date()
    date2 = date1 + timedelta(days=2*30)
    if date1 <= tday:
        print("INVALID DATE")
        return tme(f)
    elif date1 >= date2:
        print("INVALID DATE, it must be within 2 months")
        return tme(f)
    elif date1 >= tday and date1 < date2:
        pp = date1 + timedelta(days=f)
        return date1, pp
    else:
        print("INVALID DATE")
        return tme(f)

# Function for generating receipt
def check1(a, b, c, d):
    c = int(c)
    idd = ids()
    nr, cc = RN()
    day = int(input("ENTER NO OF DAYS::"))
    print("TODAY IS ::", now)
    Q, W = tme(day)
    name = input("ENTER YOUR NAME::")
    A = phn()
    AD = add()
    t = int(cc * c * day)
    day = str(day)
    print()
    ll, j, w = payments.payment(idd, t)
    if ll == 1:
        p = "Done"
        print()
        print(" @@@@@YOUR HOTEL RECEIPT@@@@@")
        print("YOUR NAME IS::", name)
        print("YOUR PHONE NUMBER IS::", A)
        print("YOUR AADHAR NO ::", AD)
        print("YOUR HOTEL IS::", a)
        print("YOUR ROOM TYPE IS::", b)
        print("YOUR TOTAL COST IS::₹", t)
        print("YOUR CHECKIN DATE IS::", Q)
        print("YOUR CHECKOUT DATE IS::", W)
        z = room(nr)
        print("YOUR ROOMS ARE::", z)
        print("YOUR BOOKING ID IS::", idd)
        print("YOUR CITY IS::", d)
        print("CHECKOUT TIME IS ::>>12:00 NOON ON", W)
        print("BOOKING IS SUCCESSFUL OF:: ₹", t)
        database.dbh(idd, name, d, A, AD, a, b, cc, z, day, t, Q, W, j, p, w)
        print(">>>>>VISIT AGAIN<<<<<")
        exit = input("PRESS ENTER TO EXIT/LOGOUT::")
    else:
        print("BOOKING FAILED___TRY AGAIN :(")
        exit = input("PRESS ENTER TO EXIT/LOGOUT::")

# Function for generating receipt
def check2(a, b, c, d):
    c = int(c)
    idd = ids()
    plat = int(input("ENTER NO OF PLATES::"))
    print("TODAY IS ::", now)
    name = input("ENTER YOUR NAME::")
    A = phn()
    tt = int(c * plat)
    print()
    ll, j, w = payments.payment(idd, tt)
    if ll == 1:
        p = "done"
        print()
        print(" @@@@@YOUR RESTAURANT RECEIPT@@@@@")
        print("YOUR NAME IS::", name)
        print("YOUR PHONE NUMBER IS::", A)
        print("YOUR FOOD TYPE IS::", a)
        print("YOUR FOOD IS::", b)
        print("YOUR NO OF PLATES ARE::", plat)
        print("YOUR TOTAL COST IS::₹", tt)
        print("YOUR BOOKING ID IS::", idd)
        print("YOUR CITY IS::", d)
        print("ORDER IS SUCCESSFUL OF:: ₹", tt)
        print("IT WILL BE DELIVERED WITHIN 15 MINUTES. HAVE PATIENCE!!.. :-)")
        database.dbr(idd, name, A, d, a, b, plat, tt, j, p, now, w)
        print(">>>>>VISIT AGAIN<<<<<")
        exit = input("PRESS ENTER TO EXIT/LOGOUT::")
    else:
        print("ORDER FAILED___TRY AGAIN :(")
        exit = input("PRESS ENTER TO EXIT/LOGOUT::")

