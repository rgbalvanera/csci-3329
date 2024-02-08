
# input message
n = int(input("Please input a number?"))

# print the stars using nested for loops
for i in range(1, n + 1):
    # print spaces
    for j in range(n - i):
        print(" ", end="")
    # print stars
    for k in range(2 * i - 1):
        print("*", end="")
    print(" ")
