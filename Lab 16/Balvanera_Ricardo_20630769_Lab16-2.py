#define the header of the bank account class
class BankAccount:
    #define the __innit__ method
    def __init__(self, initial_balance):
        self.__balance = initial_balance
#define the deposit method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited $", amount)
        else:
            print("Invalid deposit amount")
#define the withdraw  method
    def withdraw(self, amount):
        if amount > 0 and self.__balance - amount >= 0:
            self.__balance -= amount
            print("Withdrawn $", amount)
        else:
            print("Invalid withdrawal amount or insufficient funds")
#define the get_balance method
    def get_balance(self):
        return self.__balance


#create an object of the BankAccount class
account = BankAccount(100)

#test deposit and print the balance
account.deposit(200)
print("Balance after deposit:", account.get_balance())

#test withdrawing and print the balance
account.withdraw(150)
print("Balance after withdrawal:", account.get_balance())

#attempt to withdraw beyond the balance
account.withdraw(400)
print("Balance after attempting to withdraw more than balance:", account.get_balance())
