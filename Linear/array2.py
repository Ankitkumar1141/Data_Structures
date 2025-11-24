# CREATE
arr = [None]*8

arr[0] = 5
arr[1] = 10
arr[2] = 20

## READ
def read_array(arr):
    for i in range(0,len(arr)):
        print(arr[i])

## to check the number of elements present
length = 0
for i in arr:
    if i is not None:
        length += 1


## INSERT
def insert_value(arr,length,index,value):
    
    ## Check for overflow
    if length == len(arr):
        print("Array overflowed")
        return
        
    ## Check for invalid index
    if index < 0 or index > len(arr)-1:
        print("Invalid Index")
        return

    ## Update by shifting right
    if index < length:
        for i in range(length-1,index-1,-1):
            arr[i+1] = arr[i]
        arr[index] = value
        print("Sucessfully Updated")
        return

    ## Insertion at blank space
    if index > length:
        arr[index] = value
        print("Sucessfully Added")
        return


#  insert_value(arr,length,2,15) -->> Update
#  insert_value(arr,length,-2,15) -->> Invalid index
#  insert_value(arr,length,5,25)

## DELETE

def delete_value(arr, length, index):

    # Underflow check
    if length == 0:
        print("Array is empty")
        return length

    # Invalid index check
    if index < 0 or index >= length:
        print("Invalid index")
        return length

    # Shift elements LEFT
    for i in range(index, length - 1):
        arr[i] = arr[i + 1]

    # Clear last occupied element
    arr[length - 1] = None

    print("Deletion Successful")
    return length - 1

# delete_value(arr,length,1)
# delete_value(arr,length,5)
read_array(arr)