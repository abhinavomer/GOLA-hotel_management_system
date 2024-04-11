import checkout
#_FUNCTION FOR RESTAURANT_
def res(d):
    print()
    print("____/@\____WELCOME TO FOODIE CLOUD RESTAURANT____/@\____")
    print("____/@\____TYPES OF FOOD____/@\____")
    print("1.FOR INDIAN FOOD")
    print("2.FOR CHINESE FOOD")
    print("3.FOR ITALIAN FOOD")
    print("4.FOR JAPANESE FOOD")
    print("5.FOR DESERTS")
    ch1=int(input("ENTER CHOICE FOR FOOD:"))
    print()
    if ch1==1:
        print("____{TYPES OF DISHES}____")
        print("0.KAWAB PARATHA____::₹20")
        print("1.SAMOSA___COST::₹19")
        print("2.CHHOLA BHATURA___COST::₹49")
        print("3.MATAR PANEER___COST::₹349")
        print("4.FRIED RICE___COST::₹149")
        print("5.PAV BHAJI___COST::₹95")
        ch2=int(input("ENTER CHOICE FOR DISH:"))
        if ch2==0:
            a="INDIAN FOOD"
            b="KAWAB PARATHA"
            c=20
            checkout.check2(a,b,c,d)
        elif ch2==1:
            a="INDIAN FOOD"
            b="SAMOSA"
            c=19
            checkout.check2(a,b,c,d)
        elif ch2==2:
            a="INDIAN FOOD"
            b="CHHOLA BHATURA"
            c=49
            checkout.check2(a,b,c,d)
        elif ch2==3:
            a="INDIAN FOOD"
            b="MATAR PANEER"
            c=349
            checkout.check2(a,b,c,d)
        elif ch2==4:
            a="INDIAN FOOD"
            b="FRIED RICE"
            c=149
            checkout.check2(a,b,c,d)
        elif ch2==5:
            a="INDIAN FOOD"
            b="PAV BHAJI"
            c=95
            checkout.check2(a,b,c,d)
        else:
            print("INVALID CHOICE")
            res(d)
    elif ch1==2:
        print("____{TYPES OF DISHES}____")
        print("1.CHOWMEIN___COST::₹149")
        print("2.MANCHURIAN___COST::₹219")
        print("3.PASTA___COST::₹149")
        print("4.PIZZA___COST::₹269")
        print("5.MOMOS___COST::₹199")
        ch2=int(input("ENTER CHOICE FOR DISH:"))
        if ch2==1:
            a="CHINESE FOOD"
            b="CHOWMEIN"
            c=149
            checkout.check2(a,b,c,d)
        elif ch2==2:
            a="CHINESE FOOD"
            b="MANCHURIAN"
            c=219
            checkout.check2(a,b,c,d)
        elif ch2==3:
            a="CHINESE FOOD"
            b="PASTA"
            c=149
            checkout.check2(a,b,c,d)
        elif ch2==4:
            a="CHINESE FOOD"
            b="PIZZA"
            c=269
            checkout.check2(a,b,c,d)
        elif ch2==5:
            a="CHINESE FOOD"
            b="MOMOS"
            c=199
            checkout.check2(a,b,c,d)
        else:
            print("INVALID CHOICE")
            res(d)
    elif ch1==3:
       print("____{TYPES OF DISHES}____")
       print("1.ARANCINI___COST::₹149")
       print("2.LASAGNE___COST::₹219")
       print("3.PROCIUTTO___COST::₹149")
       print("4.RIBOLLITA___COST::₹269")
       print("5.SALTIMBOCCA___COST::₹199")
       ch2=int(input("ENTER CHOICE FOR DISH:"))
       if ch2==1:
           a="ITALIAN FOOD"
           b="ARANCINI"
           c=149
           checkout.check2(a,b,c,d)
       elif ch2==2:
           a="ITALIAN FOOD"
           b="LASAGNE"
           c=219
           checkout.check2(a,b,c,d)
       elif ch2==3:
            a="ITALIAN FOOD"
            b="PROCIUTTO"
            c=149
            checkout.check2(a,b,c,d)
       elif ch2==4:
            a="FOR ITALIAN FOOD"
            b="RIBOLLITA"
            c=269
            checkout.check2(a,b,c,d)
       elif ch2==5:
            a="ITALIAN FOOD"
            b="SALTIMBOCCA"
            c=199
            checkout.check2(a,b,c,d)
       else:
            print("INVALID CHOICE")
            res(d)
    elif ch1==4:
            print("____{TYPES OF DISHES}____")
            print("1.SUSHI___COST::₹149")
            print("2.TEMPURA___COST::₹219")
            print("3.OKONOMIYAKI___COST::₹149")
            print("4.SHABU SHABU___COST::₹269")
            print("5.YAKITORI___COST::₹199")
            ch2=int(input("ENTER CHOICE FOR DISH:"))
            if ch2==1:
                a="JAPANESE FOOD"
                b="SUSHI"
                c=149
                checkout.check2(a,b,c,d)
            elif ch2==2:
                a="JAPANESE FOOD"
                b="TEMPURA"
                c=219
                checkout.check2(a,b,c,d)
            elif ch2==3:
                a="JAPANESE FOOD"
                b="OKONOMIYAKI"
                c=149
                checkout.check2(a,b,c,d)
            elif ch2==4:
                a="JAPANESE FOOD"
                b="SHABU SHABU"
                c=269
                checkout.check2(a,b,c,d)
            elif ch2==5:
                a="JAPANESE FOOD"
                b="YAKITORI"
                c=199
                checkout.check2(a,b,c,d)
            else:
                print("INVALID CHOICE")
                res(d)
    elif ch1==5:
        print("____{TYPES OF DISHES}____")
        print("1.FALUDA___COST::₹49")
        print("2.KHEER___COST::₹49")
        print("3.MILK SHAKE___COST::₹99")
        print("4.KAJU BARFI___COST::₹69")
        print("5.CHHENA___COST::₹49")
        ch2=int(input("ENTER CHOICE FOR DISH:"))
        if ch2==1:
            a="DESERTS"
            b="FALUDA"
            c=49
            checkout.check2(a,b,c,d)
        elif ch2==2:
            a="DESERTS"
            b="KHEER"
            c=49
            checkout.check2(a,b,c,d)
        elif ch2==3:
            a="DESERTS"
            b="MILK SHAKE"
            c=99
            checkout.check2(a,b,c,d)
        elif ch2==4:
            a="DESERTS"
            b="KAJU BARFI"
            c=69
            checkout.check2(a,b,c,d)
        elif ch2==5:
            a="DESERTS"
            b="CHHENA"
            c=49
            checkout.check2(a,b,c,d)
        else:
            print("INVALID CHOICE")
            res(d)
    else:
        print("INVALID CHOICE")
        res(d)

        
           
