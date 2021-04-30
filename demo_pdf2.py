import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Aryapr91@",
  database="mydatabase"
)

print(mydb)
mycursor = mydb.cursor()


# Open the file with read only permit
f = open('file.txt')
# use readline() to read the first line 
line = f.readline()
# use the read line to read further.
# If the file is not empty keep reading one line
# at a time, till the file is empty
while line:
    # in python 2+
    # print line
    # in python 3 print is a builtin function, so
    print(line)
    if "QoS overview" in line:
    # use realine() to read next line
        line = f.readline()
        print(line)
        line = f.readline()
        print(line)
        line = f.readline()
        print(line)
        sql = "INSERT INTO  QOS_Configuration_Table(feature, configuration) VALUES (%s, %s)"
        val = ("QOS", line)
        mycursor.execute(sql, val)
        break;
    line = f.readline()
f.close()

mycursor.execute("SELECT * FROM QOS_Configuration_Table")

myresult = mycursor.fetchall()

for x in myresult:
	print(x) 



































































