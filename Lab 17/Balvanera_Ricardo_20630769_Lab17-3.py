#define the function header 
def insert_777(arr, j, index=9):
#terminal case
    if index == j:
        arr[index] = 777
        return arr
#recursive case
    else:
        arr[index] = arr[index - 1]
        return insert_777(arr, j, index - 1)
#define the array
array = [4, 6, 3, 8, 6, 1, 4, 7, 3, 9]
#define the index
index_to_insert = 2
#call the function
insert_777(array, index_to_insert)
#print the array
print(array)
