"""
      A python application to fetch records from SQL..:-)
"""
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="645445",database="gola")
cursor=mydb.cursor()
def con(x):
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="645445",database="gola")
        cursor=mydb.cursor()
        print("Connected to database Successfully")
        a=1
        if x==1:
            menu(a)
        elif x==2:
            menu1(a)
        else:
            pass
    except:
            print("Error in Connection")
def menu(a):
    print()
    print(">>MENU<<")
    print("1.Fetch all the Records")
    print("BY ID::")
    print("2.Fetch any specific Record::")
    print("3.Update any Record")
    print("4.Delete a Record")
    ch=int(input("Enter Your Choice(1-4)::"))
    print()
    if ch==1:
        fetchall()
    elif ch==2:
        fetchone()
    elif ch==3:
        update()
    elif ch==4:
        delete()
    else:
        print("Invalid Choice")
        a=1
        menu(a)
    q=input("PRESS ENTER TO EXIT")
def fetchall():
    print("Booking details are::")
    print("ID|Name|City|Mobile|Aadhar|Hotel|Total_r |Room_n|Days|Total_c|Check_in|Check_out|Card_no|Payment|Payment Mode")
    print()
    cursor.execute("SELECT * FROM hotel")
    data=cursor.fetchall()
    for x in data:
        print(x)
        print()
    print("Rows Affected:",cursor.rowcount)
def fetchone():
    a=int(input("Enter id::"))
    print("Booking details are::")
    cursor.execute("SELECT * FROM hotel where id=%s"%(a))
    data=cursor.fetchone()
    for x in range(1):
        print("ID::",data[0])
        print("Name::",data[1])
        print("City::",data[2])
        print("Mobile NO.:",data[3])
        print("Aadhar::",data[4])
        print("Hotel::",data[5])
        print("Room type::",data[6])
        print("Total rooms::",data[7])
        print("Room no.::",data[8])
        print("Days::",data[9])
        print("Total cost::Rs.",data[10])
        print("Check in Date::",data[11])
        print("Check out Date::",data[12])
        print("Card no::",data[13])
        print("Payment Status::",data[14])
        print("Rows Affectes:",cursor.rowcount)
def delete():
    a=int(input("Enter id::"))
    cursor.execute("DELETE FROM hotel where id=%s"%(a))
    print("Rows Affected::",cursor.rowcount)
    mydb.commit()
    mydb.close()
def update():
    print("What You Want to Update")
    print("1.Name::")
    print("2.Mobile no.::")
    print("3.Room no.::")
    ch1=int(input("Enter Choice::(1-4)"))
    a=int(input("Enter id::"))
    if ch1==1:
        b=(input("Enter New Name::"))
        q="UPDATE hotel set name='%s' WHERE id=%s"%('b',a)
    elif ch1==2:
        b=int(input("Enter New Mobile no.::"))
        q="UPDATE hotel set mobile=%s WHERE id=%s"%(b,a)
    elif ch1==3:
        b=int(input("Enter New Room no..::"))
        q="UPDATE hotel set room_n=%s WHERE id=%s"%(b,a)
    else:
        print("INVALID CHOICE")
        a=1
        menu(a)
    cursor.execute(q)
    mydb.commit()
    print("Rows Affected:",cursor.rowcount)
def menu1(a):
    print()
    print(">>MENU<<")
    print("1.Fetch all the Records")
    print("BY ID::")
    print("2.Fetch any specific Record::")
    print("3.Update any Record")
    print("4.Delete a Record")
    ch=int(input("Enter Your Choice(1-4)::"))
    print()
    if ch==1:
        fetchall1()
    elif ch==2:
        fetchone1()
    elif ch==3:
        update1()
    elif ch==4:
        delete1()
    else:
        print("Invalid Choice")
        a=1
        menu(a)
    q=input("PRESS ENTER TO EXIT")
def fetchall1():
    print("Booking details are::")
    print("ID|Name|Mobile|City|Dish Type|Dish Name|Total Plates |Total Cost|Crad no|Payment Stat.|Order Date|Payment Mode")
    print()
    cursor.execute("SELECT * FROM restaurent")
    data=cursor.fetchall()
    for x in data:
        print(x)
        print()
    print("Rows Affected:",cursor.rowcount)
def fetchone1():
    a=int(input("Enter id::"))
    print("Booking details are::")
    cursor.execute("SELECT * FROM restaurent where id=%s"%(a))
    data=cursor.fetchone()
    for x in range(1):
        print("ID::",data[0])
        print("Name::",data[1])
        print("City::",data[3])
        print("Mobile NO.:",data[2])
        print("Dish type::",data[4])
        print("Dish Name::",data[5])
        print("Total Plates::",data[6])
        print("Total Cost::",data[7])
        print("Card No.::",data[8])
        print("Payment Status::",data[9])
        print("Order Date::",data[10])
        print("Payment Mode::",data[11])
        print("Rows Affectes:",cursor.rowcount)
def delete1():
    a=int(input("Enter id::"))
    cursor.execute("DELETE FROM restaurent where id=%s"%(a))
    print("Rows Affected::",cursor.rowcount)
    mydb.commit()
    mydb.close()
def update1():
    print("What You Want to Update")
    print("1.Name::")
    print("2.Mobile no.::")
    ch1=int(input("Enter Choice::(1-2)"))
    a=int(input("Enter id::"))
    if ch1==1:
        b=(input("Enter New Name::"))
        q="UPDATE restaurent set name='%s' WHERE id=%s"%('b',a)
    elif ch1==2:
        b=int(input("Enter New Mobile no.::"))
        q="UPDATE restaurent set mobile=%s WHERE id=%s"%(b,a)
    else:
        print("INVALID CHOICE")
        a=1
        menu1(a)
    cursor.execute(q)
    mydb.commit()
    print("Rows Affected:",cursor.rowcount)
















        
    
    
