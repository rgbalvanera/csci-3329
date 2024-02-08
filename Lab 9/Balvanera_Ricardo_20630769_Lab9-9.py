
#input messages
t = int(input("Number of Test Cases?"))

#use a nested for loop for test cases
for i in range(0,t):
    #input messages
    k, n, m = map(float,input("Input:").split())
    #use an if statement to make sure you dont calculate negative numbers
    if(k < 0 or n < 0 or m < 0):
        print("Negative numbers not allowed")
    else:
        s = (k * n) - m
        print(f"The shortfall is ${s}")
