#define the function header
def check_double(arr, i=0, j=1):
    #base case: if we have checked all pairs
    if i == len(arr) - 1:
        return False
    
    #if arr[i] == 2 * arr[j], return True
    if j < len(arr) and arr[i] == 2 * arr[j]:
        return True
    
    #if we reached the end of the array, move to the next starting index
    if j == len(arr) - 1:
        return check_double(arr, i + 1, i + 2)
    
    #otherwise, increment j and continue
    return check_double(arr, i, j + 1)

# define the arrays and print the results
arr = [10, 2, 5, 3]

print(check_double(arr))  

arr = [7, 1, 14, 11]

print(check_double(arr))

arr = [3, 1, 7, 11]

print(check_double(arr))