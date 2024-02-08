import mysql.connector
from decouple import config

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=config('DB_PASSWORD'),
    database="python_test"
)

mycursor = db.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)

