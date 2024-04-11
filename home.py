"""
THIS IS A FULL HOTEL MANAGEMENT PROJECT.
"""
import login
import hotel
import credit
import data
#_MAIN_
print(" .....$$......WELCOME TO GOLA HOTEL MANAGEMENT SYSTEMS......$$.... ")
print()
print("NOTE::ALL ROOMS ARE FULLY AC WITH ALL THE LUXIRIOUS FACILITIES AND ONLINE PAYMENT ONLY :-)")
ch=(input("PRESS 1 FOR MORE INFO or ANY NUMBER FOR PROCEEDING::"))
print()
if ch=="1":
    print("1.CREDITS")
    print("2.TERMS AND CONDITIONS")
    print("3.HEADOFFICE ADDRESS AND CONTACTS")
    ch1=int(input("ENTER CHOICE::"))
    if ch1==1:
        credit.credit()
    elif ch1==2:
        credit.terms()
    elif ch1==3:
        credit.headoffice()
    else:
        print("INVALID CHOICE!!")
else:
    print("THAT'S OK!!")
print()
#_FUNCTION FOR HOMEPAGE_
def log():
    print(">>MENU<<")
    print("1.FOR PAN PACIFIC HOTELS")
    print("2.FOR FOODIE CLOUD RESTAURANTS")
    print("3.FOR DATA MODIFICATIONS")
    choice=int(input("ENTER YOUR CHOICE:"))
    if choice==1:
        hotel.hot()
    elif choice==2:
        hotel.restt()
    elif choice==3:
        print("1.OF Hotel")
        print("2.OF Restaurent")
        cc=int(input("Enter Your Choice::"))
        if cc==1:
            data.con(1)
        elif cc==2:
            data.con(2)
        else:
            print("INVALID CHOICE!!")
    else:
        print("INVALID CHOICE")
#_FUNCTION FOR LOGIN & SIGNUP_
def cc():
    print("1.LOGIN")
    print("2.SIGN UP")
    ch=int(input("ENTER CHOICE::"))
    if ch==1:
        a=login.login()
        if a==1:
            print("LOGIN SUCCESSFULLY")
            log()
        else:
            print("LOGIN FAILED")
            cc()
    elif ch==2:
        p=open("user.txt","a")
        a,b=login.pas()
        k=("\n"+a+","+b)
        p.write(k)
        p.flush()
        p.close()
        print("SIGN UP SUCCESSFULLY")
        log()
    else:
        print("INVALID CHOICE")
cc()
            
            
        

    
    
