#define the function header
def delete_element(arr, j, current_index=0):
    #if the current index equals the index j to delete
    if current_index == j:
        #shift elements to the left starting from index j
        for i in range(j, len(arr) - 1):
            arr[i] = arr[i + 1]
        #set the last element to 0
        arr[-1] = 0
    #if the current index is less than j, continue recursive call
    elif current_index < j:
        delete_element(arr, j, current_index + 1)
    else:
        #if the current index is greater than j, return the modified array
        return arr
#define the array and index
arr = [4, 6, 3, 8, 6, 1, 4, 7, 3, 9]
j = 2
#call the function
delete_element(arr, j)
#print the array
print(arr)

