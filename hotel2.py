import checkout
#_FUNCTION FOR AMRITSAR HOTELS_
def amrit(d):
    print()
    print("____[TYPES OF HOTELS]____")
    print("1.CLASSIC")
    print("2.PREMIUM")
    print()
    ch=int(input("ENTER CHOICE"))
    print()
    if ch==1:
        print("           HOTEL NAMES")
        print("1.GURU NANAK HOTEL")
        print("2.HOTEL LION")
        ch1=int(input("ENTER CHOICE FOR HOTEL:"))
        print()
        if ch1==1:
            print("____{TYPES OF ROOMS}____")
            print("1.DOUBLE BED___COST::₹4500")
            print("2.SINGLE BED____COST::₹1500")
            print()
            ch2=int(input("ENTER CHOICE FOR ROOM:"))
            if ch2==1:
                a="GURU NANAK HOTEL"
                b="DOUBLE BED"
                c=4500
                checkout.check1(a,b,c,d)
            elif ch2==2:
                a="GURU NANAK HOTEL"
                b="SINGLE BED"
                c=1500
                checkout.check1(a,b,c,d)
            else:
                print("INVALID CHOICE")
                amrit(d)
        elif ch1==2:
            print("____{TYPES OF ROOMS}____")
            print("1.DOUBLE BED___COST::₹6600")
            print("2.SINGLE BED____COST::₹2200")
            print()
            ch2=int(input("ENTER CHOICE FOR ROOM:"))
            if ch2==1:
                a="HOTEL LION"
                b="DOUBLE BED"
                c=6600
                checkout.check1(a,b,c,d)
            elif ch2==2:
                a="HOTEL LION"
                b="SINGLE BED"
                c=2200
                checkout.check1(a,b,c,d)
            else:
                print("INVALID CHOICE")
                amrit(d)
        else:
            print("INVALID CHOICE")
            amrit(d)
    elif ch==2:
        print("           HOTEL NAMES")
        print("1.VELVET HOTEL")
        print("2.HOTEL TAJ")
        ch1=int(input("ENTER CHOICE FOR HOTEL:"))
        if ch1==1:
            print("____{TYPES OF ROOMS}____")
            print("1.DOUBLE BED___COST::₹3500")
            print("2.SINGLE BED____COST::₹1500")
            print()
            ch2=int(input("ENTER CHOICE FOR ROOM:"))
            if ch2==1:
                a="VELVET HOTEL"
                b="DOUBLE BED"
                c=3500
                checkout.check1(a,b,c,d)
            elif ch2==2:
                a="VELVET HOTEL"
                b="SINGLE BED"
                c=1500
                checkout.check1(a,b,c,d)
            else:
                print("INVALID CHOICE")
                amrit(d)
        elif ch1==2:
            print("____{TYPES OF ROOMS}____")
            print("1.DOUBLE BED___COST::₹5500")
            print("2.SINGLE BED____COST::₹2500")
            print()
            ch2=int(input("ENTER CHOICE FOR ROOM:"))
            if ch2==1:
                a="HOTEL TAJ"
                b="DOUBLE BED"
                c=5500
                checkout.check1(a,b,c,d)
            elif ch2==2:
                a="HOTEL TAJ"
                b="SINGLE BED"
                c=2500
                checkout.check1(a,b,c,d)
            else:
                print("INVALID CHOICE")
                amrit(d)
        else:
            print("INVALID CHOICE")
            amrit(d)
    else:
         print("INVALID CHOICE")
         amrit(d)
