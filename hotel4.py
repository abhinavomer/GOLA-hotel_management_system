import checkout
#_FUNCTION FOR AGRA HOTELS
def agra(d):
    print()
    print("____[TYPES OF HOTELS]____")
    print("1.CLASSIC")
    print("2.PREMIUM")
    print()
    ch=int(input("ENTER CHOICE"))
    print()
    if ch==1:
        print("           HOTEL NAMES")
        print("1.LINUX")
        print("2.UNIX")
        ch1=int(input("ENTER CHOICE FOR HOTEL:"))
        print()
        if ch1==1:
            print("____{TYPES OF ROOMS}____")
            print("1.DOUBLE BED___COST::₹4500")
            print("2.SINGLE BED____COST::₹1500")
            print()
            ch2=int(input("ENTER CHOICE FOR ROOM:"))
            if ch2==1:
                a="LINUX"
                b="DOUBLE BED"
                c=4500
                checkout.check1(a,b,c,d)
            elif ch2==2:
                a="LINUX"
                b="SINGLE BED"
                c=1500
                checkout.check1(a,b,c,d)
            else:
                print("INVALID CHOICE")
                agra(d)
        elif ch1==2:
            print("____{TYPES OF ROOMS}____")
            print("1.DOUBLE BED___COST::₹6600")
            print("2.SINGLE BED____COST::₹2200")
            print()
            ch2=int(input("ENTER CHOICE FOR ROOM:"))
            if ch2==1:
                a="UNIX"
                b="DOUBLE BED"
                c=6600
                checkout.check1(a,b,c,d)
            elif ch2==2:
                a="UNIX"
                b="SINGLE BED"
                c=2200
                checkout.check1(a,b,c,d)
            else:
                print("INVALID CHOICE")
                agra(d)
        else:
            print("INVALID CHOICE")
            agra(d)
    elif ch==2:
        print("           HOTEL NAMES")
        print("1.JALSA")
        print("2.HARSHIKHAR")
        ch1=int(input("ENTER CHOICE FOR HOTEL:"))
        if ch1==1:
            print("____{TYPES OF ROOMS}____")
            print("1.DOUBLE BED___COST::₹3500")
            print("2.SINGLE BED____COST::₹500")
            print()
            ch2=int(input("ENTER CHOICE FOR ROOM:"))
            if ch2==1:
                a="JALSA"
                b="DOUBLE BED"
                c=3500
                checkout.check1(a,b,c,d)
            elif ch2==2:
                a="JALSA"
                b="SINGLE BED"
                c=1500
                checkout.check1(a,b,c,d)
            else:
                print("INVALID CHOICE")
                agra(d)
        elif ch1==2:
            print("____{TYPES OF ROOMS}____")
            print("1.DOUBLE BED___COST::₹5500")
            print("2.SINGLE BED____COST::₹2500")
            print()
            ch2=int(input("ENTER CHOICE FOR ROOM:"))
            if ch2==1:
                a="HARSHIKHAR"
                b="DOUBLE BED"
                c=5500
                checkout.check1(a,b,c,d)
            elif ch2==2:
                a="HARSHIKHAR"
                b="SINGLE BED"
                c=2500
                checkout.check1(a,b,c,d)
            else:
                print("INVALID CHOICE")
                agra(d)
        else:
            print("INVALID CHOICE")
            agra(d)
    else:
         print("INVALID CHOICE")
         agra(d)
