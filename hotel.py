import hotel0
import hotel1
import hotel2
import hotel3
import hotel4
import restaurant
#_FUNCTION FOR SHOWING HOTELS_
def hot():
    print()
    print("                            WELCOME TO PAN PACIFIC HOTELS")
    print()
    print("                              PLACES for BOOKING")
    print("LUCKNOW>>>>>1")
    print("DELHI>>>>>2")
    print("AMRITSAR>>>>>3")
    print("HARIDWAR>>>>>4")
    print("AGRA>>>>>5")
    c=int(input("ENTER CHOICE::::>"))
    print()
    if c==1:
        d="LUCKNOW"
        hotel0.lknwow(d)
    elif c==2:
        d="DELHI"
        hotel1.delhi(d)
    elif c==3:
        d="AMRITSAR"
        hotel2.amrit(d)
    elif c==4:
        d="HARIDWAR"
        hotel3.hari(d)
    elif c==5:
        d="AGRA"
        hotel4.agra(d)
    else:
        print("INVALID CHOICE")
        hot()
#_FUNCTION FOR RESTAURANT_
def restt():
    print()
    print("         WELCOME TO FOODIE CLOUD RESTAURENTS")
    print()
    print("                     PLACES for BOOKING")
    print("LUCKNOW>>>>>1")
    print("DELHI>>>>>2")
    print("AMRITSAR>>>>>3")
    print("HARIDWAR>>>>>4")
    print("AGRA>>>>>5")
    c=int(input("ENTER CHOICE::::>"))
    print()
    if c==1:
        d="LUCKNOW"
        restaurant.res(d)
    elif c==2:
        d="DELHI"
        restaurant.res(d)
    elif c==3:
        d="AMRITSAR"
        restaurant.res(d)
    elif c==4:
        d="HARIDWAR"
        restaurant.res(d)
    elif c==5:
        d="AGRA"
        restaurant.res(d)
    else:
        print("INVALID CHOICE")
        restt()


