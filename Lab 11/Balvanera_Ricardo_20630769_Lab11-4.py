#define the function header
def find_rectangle_area(M, circles):
#find min/max x coordinate radius from center x-coordinate of each circle and taking the min/max value
    min_x = min(c[0] - c[2] for c in circles)
    max_x = max(c[0] + c[2] for c in circles)
#find min/max y coordinate radius from center x-coordinate of each circle and taking the min/max value
    min_y = min(c[1] - c[2] for c in circles)
    max_y = max(c[1] + c[2] for c in circles)
    
    #calculate width and height of the rectangle
    width = max_x - min_x
    height = max_y - min_y
    #return the area of the rectangle
    return width * height

#input the number of circles
M = int(input("Enter the number of circles: "))

circles = []
for i in range(M):
    #input center coordinates and radius of each circle
    circle_data = list(map(float, input(f"Enter circle {i+1} center coordinates (x y) and radius (e.g., 0.0 0.0 0.0): ").split()))
    #append circle data to the list of circles
    circles.append(circle_data)
#call the function and find area of rectangle
area = find_rectangle_area(M, circles)
#output area of rectangle
print("Area of the rectangle: {:.2f}".format(area))

