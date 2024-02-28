'''Given a fixed length array arr (size 10) of integers, duplicate each occurrence of
k, shifting the remaining elements to the right. For example, if k = 2
Input:
arr = [0, 1, 3, 2, 4, 2, 0, 0, 0, 0]
Output:
arr = [0, 1, 3, 2, 2, 4, 2, 2, 0, 0]'''

#define the function header
def duplicate_k(arr, k, index=0):
#terminal case 
    if index >= len(arr):
        return arr
#recursive cases   
    if arr[index] == k:
        arr.insert(index, k)
        return duplicate_k(arr, k, index + 2)
    else:
        return duplicate_k(arr, k, index + 1)
    
#define the array
myarray = [0, 1, 3, 2, 4, 2, 0, 0, 0, 0]
#call the function
duplicate_k(myarray, 2,)
#print the array
print(myarray)