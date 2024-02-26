#define the function header 
def insert_777(arr, j, index=9):
    if index == j:
        arr[index] = 777
        return arr
    else:
        arr[index] = arr[index - 1]
        return insert_777(arr, j, index - 1)
#define the array
array = [4, 6, 3, 8, 6, 1, 4, 7, 3, 9]
index_to_insert = 2
insert_777(array, index_to_insert)
print(array)
