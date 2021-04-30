import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Aryapr91@",
  database="mydatabase"
)

print(mydb)
mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE mydatabase")

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

#mycursor.execute("CREATE TABLE QOS_Configuration_Table (feature VARCHAR(255), configuration VARCHAR(255))")  



mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)
  
sql = "INSERT INTO  QOS_Configuration_Table(feature, configuration) VALUES (%s, %s)"
val = ("Trust Mode", "qos trust mode dscp")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

mycursor.execute("SELECT * FROM QOS_Configuration_Table")

myresult = mycursor.fetchall()

for x in myresult:
	print(x) 