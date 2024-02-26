import mysql.connector as mc 

db = mc.connect(
    host = "35.224.230.59",
    user = "root",
    password = "1234qwer",
    database = "carmax"
)
print(db)

cursor = db.cursor()
cursor.execute("SELECT * FROM cars;")

result = cursor.fetchall()

for row in result:
    print(row)