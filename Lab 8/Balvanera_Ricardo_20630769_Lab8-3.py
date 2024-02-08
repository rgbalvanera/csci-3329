#input message
num = int(input("Please input a number? "))
print("Processing...")
#output statements with branching
if(num > 0):
    print(num, " is a positive number")
elif(num < 0):
    print(num, " is a negative number")
else:
    print(num, " is equal to zero")
