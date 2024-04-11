#_FUNCTION FOR PAYMENT_
import getpass
def chcv():
     c=getpass.getpass("Enter cvv::")
     if len(c)==3:
          return c
     else:
          print("INVALID CVV")
          print("CVV MUST BE OF 3 LETTERS")
          return chcv()
def cvv():
     c=chcv()
     d=getpass.getpass("Confirm cvv::")
     e=c
     while d!=c:
          print("Check cvv!!")
          c=getpass.getpass("Enter cvv::")
          d=getpass.getpass("Confirm cvv::")
     return d,c
def payment(idd,s):
     import random
     import getpass	
     l=random.randint(100000,999999)
     p=random.randint(100000,999999)

     print("..........................Pay  through............................")
     m=int(input("1.FOR DEBIT CARD or  2.FOR CREDIT CARD::"))
     if m==2:
          print("                          CREDIT CARD MODE")                            
          w="Credit Card"
          print("YOUR ID IS ::",idd)
          print("YOUR PAYMENT AMOUNT IS::₹",s)
          a=str(input("Enter name::"))
          b=str(input("Enter CREDIT card no(16 Digits)::"))
          while len(b)!=16 or b.isdigit()==False:
              print ("Invalid cardno!!")
              b=str(input("Enter card no(16 digits)::"))
          if len(b)==16:
               d,c=cvv()
               if d==c:
                           print('Your otp:::',l)
                           j=int(input('Enter otp::'))
                           while j!=l:
                                                  l=random.randint(100000,999999)
                                                  print('Invalid otp')
                                                  print('New otp::',l)
                                                  j=int(input('Enter otp::'))
                           if j==l:
                                return 1,b,w
     if m==1:
          print("                           DEBIT CARD MODE")
          w="Debit Card"
          print("YOUR ID IS ::",idd)
          print("YOUR PAYMENT AMOUNT IS::₹",s)
          a=str(input("Enter name::"))
          b=str(input("Enter card no(16 digits)::"))
          while len(b)!=16 or b.isdigit()==False:
              print ("Invalid cardno!!")
              b=str(input("Enter card no(16 digits)::"))
          if len(b)==16:
               d,c=cvv()
               if d==c:
                   print('Your otp::',l)
                   j=int(input('Enter otp::'))
                   while j!=l:
                        l=random.randint(100000,999999)
                        print('Invalid otp')
                        print('New otp:::',l)
                        j=int(input('Enter otp::'))
                   if j==l:
                        return 1,b,w
     else:
          payment(idd,s)
