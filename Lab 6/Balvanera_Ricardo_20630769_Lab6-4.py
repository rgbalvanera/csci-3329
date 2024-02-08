import math
#input message for height
h = float(input("Please input the height of the cylinder? "))
#input message for radius 
r = float(input("Please input the radius of the cylinder? "))
#calculate volume
v = math.pi * (r * r) * h
#output message for volume
print("The volume of the cylinder is: ", v)