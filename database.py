import mysql.connector
def dbh(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p):
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="645445",database="gola")
    db=mydb.cursor()
    z="INSERT INTO hotel(`id`, `name`, `city`, `mobile`, `aadhar`, `hotel`, `room_type`, `total_rooms`, `room_n`,`days`,`total`,`check_in`, `check_out`, `card_no`, `payment`,`payment_mod`) VALUES({},'{}','{}','{}','{}','{}','{}','{}','{}','{}',{},'{}','{}','{}','{}','{}')"
    db.execute(z.format(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p))
    mydb.commit()
    mydb.close()
def dbr(a,b,c,d,e,f,g,h,i,j,k,l):
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="645445",database="gola")
    db=mydb.cursor()
    z="INSERT INTO restaurent(`id`, `name`, `mobile_no`, `city`, `dish_type`, `dish_name`, `total_plates`, `total`, `card_no`, `payment`,`order_date`,`payment_mod`) VALUES ({},'{}','{}','{}','{}','{}','{}',{},'{}','{}','{}','{}')"
    db.execute(z.format(a,b,c,d,e,f,g,h,i,j,k,l))
    mydb.commit()
    mydb.close()
    
