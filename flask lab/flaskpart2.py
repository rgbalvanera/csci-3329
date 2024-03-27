from flask import Flask, render_template
import mysql.connector as mc

app = Flask(__name__)

db = mc.connect(host="cs3320.myswl.database.azure.com", user="newuser", pssword = "zxcv1234!",database="db1")

cursor = db.cursor()
cursor.execute("select * from cars;")
rows = cursor.fetchall()

@app.route('/result')
def result():
 dict = {'phy':50,'che':60,'maths':70}
 return render_template('result.html',
result = dict)

if __name__ == '__main__':
 app.run(debug = True)