import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="cursist",
  passwd="cursist",
  database="test"
)
mycursor = mydb.cursor()

def read(customerId):
    sql = "select * from customers where id = %s"
    val = (customerId,)
    mycursor.execute(sql, val)

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

def readAll():
    sql = "select * from customers"
    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)


def create(name, adress):
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = (name, adress)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

