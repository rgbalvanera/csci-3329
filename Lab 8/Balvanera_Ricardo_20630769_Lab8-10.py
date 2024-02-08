#import any libraries necessary
import math
#input origin of circle
x, y = map(int,input("What is the origin of the circle?").split())
#input radius
r = int(input("What is the radius? "))
#input two points on a line
#for the sake of understanding the code, x1 y1 is point A and x2 y2 is point B
x1, y1, x2, y2 = map(int,input("What are two points on a line? ").split())
#calculate area of the circle
#step 1 get the area of the original circle, before cutting 
og_area = math.pi * (r ** 2)
#step 2 get the three distances from the origin and the two coordinate points
    #distance from point a and point b
d1 = float(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)
    #distance from point b to the origin
d2 = float(((x2 - x) ** 2 + (y2 - y) ** 2) ** 0.5)
    #distance from point a to the origin
d3 = float(((x1 - x) ** 2 + (y1 - y) ** 2) ** 0.5)
#step 3 get the angle of the segment that is located at the radius
angle = math.acos((d3**2 + d1**2 - d2**2) / (2 * d3 * d1))
#step 4 we now have our angle, use that to calculate the area of the segment
segment_area = (angle - math.sin(angle) / 2) * (r**2)
#step 5 subtract the areas and output result
new_area = og_area - segment_area
print("The area of the larger resulting shape is", new_area)
