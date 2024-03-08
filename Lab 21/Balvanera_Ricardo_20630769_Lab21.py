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

query = "INSERT INTO cars VALUES ( %S , %S , %S , %S , %S , %S , %S )"

values = [('3AE9K', 'Honda','Accord',2019,5847,19000,'Silver'),
          ('GT123','Toyota','Camry',2008,70000,8000,'Black'),
          ('AB382','Honda','Accord',2014,10000,18000,'White'),
          ('Y3829','Hyundai','Sonata',2013,20000,17000,'Silver'),
          ('4TX88','Ford','F150',2017,12,38500,'Red')]
cursor.executemany(query,values)

db.commit()

print(cursor.rowcount, "record inserted")