import math
#input first end point
x1, y1 = map(float,input("Please input the first endpoint: ").split())
#input second end point
x2, y2 = map(float,input("Please input the second endpoint: ").split())
#calculate length
length = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
#print length
print("The length is ", length)