#import any libraries necessary
import math
#define the function header
def calculate_area(x1, y1, x2, y2,x3, y3):
    #calculate distances
  #distance from point 1 to 2
    d1 = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
  #distance from point 2 to 3
    d2 = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5
  #distance from point 1 to 3
    d3 = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
#calculate semiperimeter (sp for short)
    sp = (d1 + d2 + d3) / 2
#calculate area
    area = float(math.sqrt(sp * (sp - d1) * (sp - d2) * (sp - d3)))
#return the area
    return(area)

#input statement
x1, y1, x2, y2, x3, y3 = map(int, input("Please input three points:").split())
#output statement
print("The area is {:.2f}".format(calculate_area(x1, y1, x2, y2,x3, y3)))