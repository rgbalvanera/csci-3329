#input statement
l1, l2, l3 = map(int, input("Please input lenghths of three line segments: ").split())
#calculate and output statement
if(l1+l2 > l3 and l1+l3 > l2 and l2+13 > l1):
    print("Yes")
else:
    print("No")