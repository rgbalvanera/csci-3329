
#input message
n = int(input("Please input a number? "))

#print the stars using nested for loops
for i in range(0, n):
    # print spaces
    for j in range(0, i):
        print(" ", end="")
    # print stars
    for j in range(0, n - i):
        print("*", end="")
    print(" ")