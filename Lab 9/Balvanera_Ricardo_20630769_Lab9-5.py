#input message
num = int(input("Enter a number: "))
#print stars using nested for loops
for i in range(0,num):
  for j in range(0,i+1):
    print("*",end=" ")
  print("")