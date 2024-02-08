#input statement
n = int(input("Please input a number?"))
#print multiplication table using a nested for loop
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j * i, end=" ")
    print("")