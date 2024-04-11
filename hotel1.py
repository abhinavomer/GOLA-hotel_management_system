import checkout
#_FUNCTION FOR DELHI HOTELS_
def delhi(d):
    print()
    print("____[TYPES OF HOTELS]____")
    print("1.CLASSIC")
    print("2.PREMIUM")
    print()
    ch=int(input("ENTER CHOICE"))
    print()
    if ch==1:
        print("           HOTEL NAMES")
        print("1.GRAND HOTEL")
        print("2.HOTEL ROYALE")
        ch1=int(input("ENTER CHOICE FOR HOTEL:"))
        print()
        if ch1==1:
            print("____{TYPES OF ROOMS}____")
            print("1.DOUBLE BED___COST::₹4500")
            print("2.SINGLE BED____COST::₹1500")
            print()
            ch2=int(input("ENTER CHOICE FOR ROOM:"))
            if ch2==1:
                a="GRAND HOTEL"
                b="DOUBLE BED"
                c=4500
                checkout.check1(a,b,c,d)
            elif ch2==2:
                a="GRAND HOTEL"
                b="SINGLE BED"
                c=1500
                checkout.check1(a,b,c,d)
            else:
                print("INVALID CHOICE")
                delhi(d)
        elif ch1==2:
            print("____{TYPES OF ROOMS}____")
            print("1.DOUBLE BED___COST::₹6600")
            print("2.SINGLE BED____COST::₹2200")
            print()
            ch2=int(input("ENTER CHOICE FOR ROOM:"))
            if ch2==1:
                a="HOTEL ROYALE"
                b="DOUBLE BED"
                c=6600
                checkout.check1(a,b,c,d)
            elif ch2==2:
                a="HOTEL ROYALE"
                b="SINGLE BED"
                c=2200
                checkout.check1(a,b,c,d)
            else:
                print("INVALID CHOICE")
                delhi(d)
        else:
            print("INVALID CHOICE")
            delhi(d)
    elif ch==2:
        print("           HOTEL NAMES")
        print("1.CLASSIO HOTEL")
        print("2.HOTEL PEARL")
        ch1=int(input("ENTER CHOICE FOR HOTEL:"))
        if ch1==1:
            print("____{TYPES OF ROOMS}____")
            print("1.DOUBLE BED___COST::₹3500")
            print("2.SINGLE BED____COST::₹500")
            print()
            ch2=int(input("ENTER CHOICE FOR ROOM:"))
            if ch2==1:
                a="CLASSIO HOTEL"
                b="DOUBLE BED"
                c=3500
                checkout.check1(a,b,c,d)
            elif ch2==2:
                a="CLASSIO HOTEL"
                b="SINGLE BED"
                c=1500
                checkout.check1(a,b,c,d)
            else:
                print("INVALID CHOICE")
                delhi(d)
        elif ch1==2:
            print("____{TYPES OF ROOMS}____")
            print("1.DOUBLE BED___COST::₹5500")
            print("2.SINGLE BED____COST::₹2500")
            print()
            ch2=int(input("ENTER CHOICE FOR ROOM:"))
            if ch2==1:
                a="HOTEL PEARL"
                b="DOUBLE BED"
                c=5500
                checkout.check1(a,b,c,d)
            elif ch2==2:
                a="HOTEL PEARL"
                b="SINGLE BED"
                c=2500
                checkout.check1(a,b,c,d)
            else:
                print("INVALID CHOICE")
                delhi(d)
        else:
            print("INVALID CHOICE")
            delhi(d)
    else:
         print("INVALID CHOICE")
         delhi(d)
