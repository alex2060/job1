#mysql.server start
#mysql -u root -p
#pass
#USE job1
#CREATE USER 'leroy'@'localhost' IDENTIFIED BY 'jankans';
#GRANT ALL PRIVILEGES ON job1.* TO 'leroy'@'localhost';

#CREATE TABLE `testdata` ( `testing` INT NOT NULL ) ENGINE = InnoDB;
#INSERT INTO `testdata` (`testing`) VALUES ('6');
#select * from testdata;
#CREATE TABLE `test2` ( `name` TEXT NOT NULL , `key` TEXT NOT NULL ) ENGINE = InnoDB;
#INSERT INTO `test2` (`name`, `key`) VALUES ('hey', 'now');
#INSERT INTO `test2` (`name`, `key`) VALUES ('we', 'go');


#users username text , password text, creation date , email

#CREATE TABLE `job_usertable` ( `username` TEXT NOT NULL , `password` TEXT NOT NULL , `creation` TIMESTAMP NOT NULL , `email` TEXT NOT NULL , PRIMARY KEY (`username`(248))) ENGINE = InnoDB;
#INSERT INTO `job_usertable` (`username`, `password`, `creation`, `email`) VALUES ('my', 'user', CURRENT_TIMESTAMP, 'alex.haussmann@gmail.com');
#SELECT * FROM `job_usertable` WHERE `username` LIKE 'my';
#select * from job_usertable;



#money user text , amont_of_money float  , money_type float , acount_id
#CREATE TABLE `money` ( `user` TEXT NOT NULL , `user_money` TEXT NOT NULL , `mony_type` TEXT NOT NULL , `amount_of_money` FLOAT NOT NULL , PRIMARY KEY (`user_money`(248))) ENGINE = InnoDB;
#INSERT INTO `money` (`user`, `user_money`, `mony_type`, `amount_of_money`) VALUES ('myuser', 'myuser_money1', 'money1', '10');
#UPDATE `money` SET `amount_of_money` = '11' WHERE `money`.`user_money` = 'myuser_money1';




#traidtable traid_id int, traid mony_type ,traid_money_amount , user , traid_request_money_type , traid_request_money_amount , buyer text 
#CREATE TABLE `traidtable` ( `traid_id` TEXT NOT NULL , `traid_mony_type` TEXT NOT NULL , `traid_request_type` TEXT NOT NULL , `traid_request_amount` FLOAT NOT NULL , `traid_money_amount` FLOAT NOT NULL , `user` TEXT NOT NULL , `buyer` TEXT NOT NULL , PRIMARY KEY (`traid_id`(248))) ENGINE = InnoDB;

#INSERT INTO `traidtable` (`traid_id`, `traid_mony_type`, `traid_request_type`, `traid_request_amount`, `traid_money_amount`, `user`, `buyer`) VALUES ('traidid', 'money_type_traid', 'money_raided', '10', '23', 'user', 'NULL');

#UPDATE `traidtable` SET `buyer` = 'someone' WHERE `traidtable`.`traid_id` = 'traidid';



#transation table traid_id, main_id, moneytype1,moneytype2, moneyamount1, moneyamount2 


#convertion rate money1, money2 , rate , base





#function makeuseremail (uname,email,password)


#function check_user (uname , password) return true/false

#view traid(traid_id)


#view useracount(username,pasword)

#funtion log_traid(traid_id) puts traid in transation table adds it to convertion rate table


#funtion compleat traid (traid_id,username,password):


#funtion maketraid (username, password , traid_money_type,traid_money_amount,request_money_type,request_amount )


def pyspark_datagetter():
	from pyspark.sql import SparkSession
	from pyspark.sql.functions import col

	spark = SparkSession\
	    .builder\
	    .appName("Word Count")\
	    .config("spark.driver.extraClassPath", "mysql.jar")\
	    .getOrCreate()

	dataframe_mysql = spark.read\
	    .format("jdbc")\
	    .option("url", "jdbc:mysql://localhost/job1")\
	    .option("driver", "com.mysql.jdbc.Driver")\
	    .option("dbtable", "test2").option("user", "leroy")\
	    .option("password", "jankans").load()

	#print(dataframe_mysql.columns)
	rows = dataframe_mysql.select(col('name'),col('key')).collect()
	final_list = []
	for i in rows:
	    final_list.append([i[0],i[1]])
	name=dataframe_mysql.toPandas()
	#print(name["key"].sort_values())


import mysql.connector

def makeuseremail(uname,email,password):
	cnx = mysql.connector.connect(user='leroy', password='jankans',
                              host='localhost',
                              database='job1')

	Q1=("SELECT * FROM `job_usertable` WHERE `username` LIKE \'"+uname+"\';")
	cursor = cnx.cursor(buffered=True)
	cursor.execute(Q1)
	counter=0
	for row in cursor:
		counter=counter+1
	if counter!=0:
		return "user taken"
	query = ("INSERT INTO `job_usertable` (`username`, `password`, `creation`, `email`) VALUES (\'"+uname+"\', \'"+password+"\', CURRENT_TIMESTAMP, \'"+email+"\');")
	#print(query)
	cursor = cnx.cursor(buffered=True)
	cursor.execute(query)
	cnx.commit()
	
	query2=("INSERT INTO `money` (`user`, `user_money`, `mony_type`, `amount_of_money`) VALUES (\'"+uname+"\', \'"+uname+"_money1\', 'money1', '1000');")
	cursor = cnx.cursor(buffered=True)
	cursor.execute(query2)
	cnx.commit()

	query3=("INSERT INTO `money` (`user`, `user_money`, `mony_type`, `amount_of_money`) VALUES (\'"+uname+"\', \'"+uname+"_money2\', 'money2', '1000');")
	cursor = cnx.cursor(buffered=True)
	cursor.execute(query3)
	cnx.commit()
	cnx.close()

	return "added user"



def usercheck(uname,password):
	cnx = mysql.connector.connect(user='leroy', password='jankans',
                              host='localhost',
                              database='job1')
	Q1=("SELECT * FROM `job_usertable` WHERE `username` LIKE \'"+uname+"\' AND `password` LIKE \'"+password+"\'")
	cursor = cnx.cursor(buffered=True)
	cursor.execute(Q1)
	counter=0
	for row in cursor:
		counter=counter+1
	cnx.close()
	if counter!=0:
		return "True"
	return "False"



import random
import string

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    #print(letters)
    result_str=""
    for x in range(length):
    	result_str=result_str+random.choice(letters)
    return result_str


def usercheck_conect(uname,password,cnx):
	Q1=("SELECT * FROM `job_usertable` WHERE `username` LIKE \'"+uname+"\' AND `password` LIKE \'"+password+"\'")
	cursor = cnx.cursor(buffered=True)
	cursor.execute(Q1)
	counter=0
	for row in cursor:
		counter=counter+1
	if counter!=0:
		return "True"
	return "False"


def funtion_make_traid(username, password ,traid_money_type,traid_money_amount,request_money_type,request_amount ):
	cnx = mysql.connector.connect(user='leroy', password='jankans',
                              host='localhost',
                              database='job1')
	is_user=usercheck_conect(username,password,cnx)
	if is_user=="False":
		return "wrong_username"
	traidid=get_random_string(64)


	Q0=("SELECT `amount_of_money` FROM `money` WHERE `user_money` LIKE \'"+username+"_"+traid_money_type+"\'")

	cursor = cnx.cursor(buffered=True)
	cursor.execute(Q0)

	for row in cursor:
		money=row[0]

	amnountleft=money-traid_money_amount
	if amnountleft>0:
		#print("we good")
		#print(amnountleft)
		pass
	else:
		return "nofunds"


	U1=("UPDATE `money` SET `amount_of_money` = \'"+str(amnountleft)+"\' WHERE `money`.`user_money` = '"+username+"_"+traid_money_type+"';")

	cursor = cnx.cursor(buffered=True)
	cursor.execute(U1)
	cnx.commit()

	Q1=("INSERT INTO `traidtable` (`traid_id`, `traid_mony_type`, `traid_request_type`, `traid_request_amount`, `traid_money_amount`, `user`, `buyer`) VALUES (\'"+traidid+"\', \'"+traid_money_type+"\', \'"+request_money_type+"\', \'"+str(request_amount)+"\', \'"+str(traid_money_amount)+"\', \'"+username+"\', 'NULL');")
	cursor = cnx.cursor(buffered=True)
	cursor.execute(Q1)
	cnx.commit()
	counter=0
	cnx.close()
	return traidid+" "+str(amnountleft)


def compleat_traid(user,password,traid_id):
	cnx = mysql.connector.connect(user='leroy', password='jankans',
                              host='localhost',
                              database='job1')

	is_user=usercheck_conect(user,password,cnx)
	if is_user=="False":
		return "wrong_username"

	sql=("SELECT `traid_mony_type`,`traid_request_type`,`traid_request_amount`,`traid_money_amount`,`buyer`,`user` FROM `traidtable` WHERE `traid_id` LIKE \'"+traid_id+"\';")
	cursor = cnx.cursor(buffered=True)
	cursor.execute(sql)
	for row in cursor:
		traid_mony_type=row[0]
		traid_request_type=row[1]
		traid_request_amount=row[2]
		traid_money_amount=row[3]
		buyer=row[4]
		reciver=row[5]


	#substack form payied user
	Q0=("SELECT `amount_of_money` FROM `money` WHERE `user_money` LIKE \'"+user+"_"+traid_request_type+"\'")

	cursor = cnx.cursor(buffered=True)
	cursor.execute(Q0)

	for row in cursor:
		money=row[0]

	amnountleft=money-traid_request_amount
	if amnountleft>0:
		pass
	else:
		return "nofunds"

	U1=("UPDATE `money` SET `amount_of_money` = \'"+str(amnountleft)+"\' WHERE `money`.`user_money` = '"+user+"_"+traid_request_type+"';")

	cursor = cnx.cursor(buffered=True)
	cursor.execute(U1)
	cnx.commit()








	#put money gained form train to taker of traid
	Q0=("SELECT `amount_of_money` FROM `money` WHERE `user_money` LIKE \'"+reciver+"_"+traid_request_type+"\'")
	cursor = cnx.cursor(buffered=True)
	cursor.execute(Q0)

	for row in cursor:
		money=row[0]

	amnountleft=money+traid_request_amount


	U1=("UPDATE `money` SET `amount_of_money` = \'"+str(amnountleft)+"\' WHERE `money`.`user_money` = '"+reciver+"_"+traid_request_type+"';")
	cursor = cnx.cursor(buffered=True)
	cursor.execute(U1)





	#add to user acount who made traid

	Q0=("SELECT `amount_of_money` FROM `money` WHERE `user_money` LIKE \'"+user+"_"+traid_mony_type+"\'")

	cursor = cnx.cursor(buffered=True)
	cursor.execute(Q0)

	for row in cursor:
		money=row[0]

	amnountleft=money+traid_money_amount


	U1=("UPDATE `money` SET `amount_of_money` = \'"+str(amnountleft)+"\' WHERE `money`.`user_money` = '"+user+"_"+traid_mony_type+"';")
	cursor = cnx.cursor(buffered=True)
	cursor.execute(U1)
	cnx.commit()




	#update buyer


	Q0=("UPDATE `traidtable` SET `buyer` = \'"+user+"\' WHERE `traidtable`.`traid_id` = \'"+traid_id+"\';")
	cursor = cnx.cursor(buffered=True)
	cursor.execute(Q0)
	cnx.commit()
	cnx.close()


	#print(traid_mony_type,traid_request_type,traid_request_amount,traid_money_amount,buyer,reciver)
	return traid_id;




def user_acount(user,delininator):
	cnx = mysql.connector.connect(user='leroy', password='jankans',
                              host='localhost',
                              database='job1')
	outsting=""
	Q0=("SELECT `user_money`,`amount_of_money` FROM `money` WHERE `user` LIKE \'"+user+"\'")
	cursor = cnx.cursor(buffered=True)
	cursor.execute(Q0)
	cnx.commit()
	for row in cursor:
		outsting=outsting+row[0]+", "+str(row[1])+delininator
	cnx.commit()
	return outsting





def log_traid(traid_id):
	cnx = mysql.connector.connect(user='leroy', password='jankans',
                          host='localhost',
                          database='job1')

	sql=("SELECT `traid_mony_type`,`traid_request_type`,`traid_request_amount`,`traid_money_amount`,`buyer`,`user` FROM `traidtable` WHERE `traid_id` LIKE \'"+traid_id+"\';")
	cursor = cnx.cursor(buffered=True)
	cursor.execute(sql)
	for row in cursor:
		traid_mony_type=row[0]
		traid_request_type=row[1]
		traid_request_amount=row[2]
		traid_money_amount=row[3]
	reciveto_convert_amount=traid_money_amount/traid_request_amount
	otherway=traid_request_amount/traid_money_amount
	


















print(makeuseremail("uname3money","email","password"))
print(usercheck("uname1","password1"))
my_traid=funtion_make_traid("uname3money", "password" ,"money1",1,"money2",2 )
vals = my_traid.split(" ")
print(vals)

print(makeuseremail("traid_uname3money","email","password1"))


print(vals[0])

print(compleat_traid("traid_uname3money","password1",vals[0]))

myacount=user_acount("traid_uname3money","\n")
print(myacount)
#pyspark_datagetter()

print("done")

