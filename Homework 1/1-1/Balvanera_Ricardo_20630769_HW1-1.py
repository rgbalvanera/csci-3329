#define the function header that will check intersection
def check_intersection(x1, y1, x2, y2, x3, y3, x4, y4):
#calculate slopes of the two lines
    slope1 = (y2 - y1) / (x2 - x1) if x2 - x1 != 0 else float('inf')
    slope2 = (y4 - y3) / (x4 - x3) if x4 - x3 != 0 else float('inf')
#ceck if the slopes are different (lines are not parallel)
    if slope1 != slope2:
#calculate intersection point
        intersection_x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / \
                         ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
        intersection_y = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / \
                         ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))

#check if intersection point is within both line segments
        if (min(x1, x2) <= intersection_x <= max(x1, x2) and
            min(y1, y2) <= intersection_y <= max(y1, y2) and
            min(x3, x4) <= intersection_x <= max(x3, x4) and
            min(y3, y4) <= intersection_y <= max(y3, y4)):
#if lines intersect, the program will return 1, otherwise it'll return 0
            return 1
        else:
            return 0  
    else:
        return 0 
#open both the input and output files 
input_file = open("input.txt", "r")
output_file = open("output.txt", "a")
#get the number of test cases from the input file
num_test_cases = int(input_file.readline().strip())
#get the xy coordinates for each test case
for _ in range(num_test_cases):
  x1, y1, x2, y2, x3, y3, x4, y4 = map(int,input_file.readline().split())
#call the function 
  output_file.write(str(check_intersection(x1, y1, x2, y2, x3, y3, x4, y4))+ "\n")
#close the files
input_file.close()
output_file.close()