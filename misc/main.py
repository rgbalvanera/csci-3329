'''import mysql.connector as mc

db = mc.connect(host="cs3329.mysql.database.azure.com", 
                user="newuser",
                passwd="zxcy1234!"
                ,database="db1")
'''
import threading
import time
import random


class account:
    def __init__(self,balance):
        self.balance = balance

    def deposit(self, m):
        self.balance += m

class myThread(threading.Thread):
    def __init__(self,name,acc):
        threading.Thread.__init__(self)
        self.name = name
        self.acc = acc

    def run(self):
        for i in range(20):
            self.acc.deposit(1)
            time.sleep(random.random())

a = account(0)

thread1 = myThread("KIM", a)
thread2 = myThread("Park",a)

thread1.start()
thread2.start()