#input message
num = int(input("Please input a number? "))
#even or odd
if(num % 2 == 0):
    ans = "even" 
else:
    ans = "odd"
#output message
print(num, " is an " , ans, " number")