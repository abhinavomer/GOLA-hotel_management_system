import checkout
#_FUNCTION FOR LUCKNOW HOTELS_
def lknwow(d):
    print()
    print("____[TYPES OF HOTELS]____")
    print("1.CLASSIC")
    print("2.PREMIUM")
    print()
    ch=int(input("ENTER CHOICE"))
    print()
    if ch==1:
        print("           HOTEL NAMES")
        print("1.RED HOTEL")
        print("2.HOTEL SYMPATHY")
        ch1=int(input("ENTER CHOICE FOR HOTEL:"))
        print()
        if ch1==1:
            print("____{TYPES OF ROOMS}____")
            print("1.DOUBLE BED___COST::₹4500")
            print("2.SINGLE BED____COST::₹1500")
            print()
            ch2=int(input("ENTER CHOICE FOR ROOM:"))
            if ch2==1:
                a="RED HOTEL"
                b="DOUBLE BED"
                c=4500
                checkout.check1(a,b,c,d)
            elif ch2==2:
                a="RED HOTEL"
                b="SINGLE BED"
                c=1500
                checkout.check1(a,b,c,d)
            else:
                print("INVALID CHOICE")
                lknwow(d)
        elif ch1==2:
            print("____{TYPES OF ROOMS}____")
            print("1.DOUBLE BED___COST::₹6600")
            print("2.SINGLE BED____COST::₹2200")
            print()
            ch2=int(input("ENTER CHOICE FOR ROOM:"))
            if ch2==1:
                a="HOTEL SYMPATHY"
                b="DOUBLE BED"
                c=6600
                checkout.check1(a,b,c,d)
            elif ch2==2:
                a="HOTEL SYMPATHY"
                b="SINGLE BED"
                c=2200
                checkout.check1(a,b,c,d)
            else:
                print("INVALID CHOICE")
                lknwow(d)
        else:
            print("INVALID CHOICE")
            lknwow(d)
    elif ch==2:
        print("           HOTEL NAMES")
        print("1.FORT HOTEL")
        print("2.HOTEL PALACE")
        ch1=int(input("ENTER CHOICE FOR HOTEL:"))
        if ch1==1:
            print("____{TYPES OF ROOMS}____")
            print("1.DOUBLE BED___COST::₹3500")
            print("2.SINGLE BED____COST::₹1500")
            print()
            ch2=int(input("ENTER CHOICE FOR ROOM:"))
            if ch2==1:
                a="FORT HOTEL"
                b="DOUBLE BED"
                c=3500
                checkout.check1(a,b,c,d)
            elif ch2==2:
                a="FORT HOTEL"
                b="SINGLE BED"
                c=1500
                checkout.check1(a,b,c,d)
            else:
                print("INVALID CHOICE")
                lknwow(d)
        elif ch1==2:
            print("____{TYPES OF ROOMS}____")
            print("1.DOUBLE BED___COST::₹5500")
            print("2.SINGLE BED____COST::₹2500")
            print()
            ch2=int(input("ENTER CHOICE FOR ROOM:"))
            if ch2==1:
                a="HOTEL PALACE"
                b="DOUBLE BED"
                c=5500
                checkout.check1(a,b,c,d)
            elif ch2==2:
                a="HOTEL PALACE"
                b="SINGLE BED"
                c=2500
                checkout.check1(a,b,c,d)
            else:
                print("INVALID CHOICE")
                lknwow(d)
        else:
            print("INVALID CHOICE")
            lknwow(d)
    else:
         print("INVALID CHOICE")
         lknwow(d)
            
            
      
                

                
