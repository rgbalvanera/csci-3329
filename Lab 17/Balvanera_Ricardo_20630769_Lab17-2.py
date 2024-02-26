#define the function header
def consecutive_ones(arr):
    current_count = 0
    counts = []
#loop through the array
    for i in arr:
#if the number is 1, the current count will go up by one
        if i == 1:
            current_count += 1
#otherwise it will add it to the list of counts, and reset the count to 0
        elif i == 0:
            counts.append(current_count)
            current_count = 0
#return the highest count (highest number of consecutive 1s)
    return max(counts)
#define the array
myarray = [1, 1, 0, 1, 1, 1, 0, 0, 1, 1]   
#call the function and print
print(consecutive_ones(myarray))