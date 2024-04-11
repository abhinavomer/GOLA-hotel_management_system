import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="645445",database="gola")
db=mydb.cursor()
z="CREATE TABLE `gola`.`hotel` (`id` INT NOT NULL,`name` VARCHAR(45) NOT NULL,`city` VARCHAR(45) NOT NULL,`mobile` VARCHAR(45) NOT NULL,`aadhar` VARCHAR(45) NOT NULL,`hotel` VARCHAR(45) NOT NULL, `room_type` VARCHAR(45) NOT NULL,`total_rooms` VARCHAR(45) NOT NULL,`room_n` VARCHAR(45) NOT NULL,`days` INT NOT NULL,`total` INT NOT NULL,`check_in` DATE NOT NULL,`check_out` DATE NOT NULL,`card_no` VARCHAR(45) NOT NULL,`payment` VARCHAR(45) NOT NULL,`payment_mod` VARCHAR(45) NOT NULL,PRIMARY KEY (`id`));"
db.execute(z)
j="CREATE TABLE `gola`.`restaurent` (`id` INT NOT NULL,`name` VARCHAR(45) NOT NULL,`mobile_no` VARCHAR(45) NOT NULL,`city` VARCHAR(45) NOT NULL,`dish_type` VARCHAR(45) NOT NULL,`dish_name` VARCHAR(45) NOT NULL,`total_plates` VARCHAR(45) NOT NULL,`total` INT NOT NULL,`card_no` VARCHAR(45) NOT NULL,`payment` VARCHAR(45) NOT NULL,`order_date` VARCHAR(45) NOT NULL,`payment_mod` VARCHAR(45) NOT NULL,PRIMARY KEY (`id`));"
db.execute(j)
mydb.commit()
mydb.close()
