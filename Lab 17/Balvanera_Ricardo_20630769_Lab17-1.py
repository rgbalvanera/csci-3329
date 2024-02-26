#define the function header
def number_of_even(arr):
    count = 0
    for i in arr:
        if i % 2 == 0:
            count += 1
    return count
#define the array
myarray = [17, 462, 4, 5, 8575]
#call the function and print
print(number_of_even(myarray))