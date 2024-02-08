#input statement
sides = [int(i) for i in input("Input:").split()]
#determine if rectangle and output if condition is True
if (sides[0] == sides[1] and sides[2] == sides[3]):
    print("YES")
elif(sides[0] == sides[2] and sides[1] == sides[3]):
    print("YES")
elif(sides[0] == sides[3] and sides[1] == sides[2]):
    print("YES")
else:
    print("NO")