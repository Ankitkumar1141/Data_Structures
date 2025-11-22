arr = [2,4,6]  ## Blank array

## CREATE

arr.insert(0,5) # insert an element in the beginning of an array -- insert(index,value)

arr.append(8) # insert an element at the last of an array

arr.insert(5,10)

arr1 = [3,7,9,1]

arr = arr + arr1 ## combining two different arrays

## READ

print(arr) ## read whole array

print(arr[0]) ## read first element of an array

print(arr[-1]) ## read last element of an array

print(arr[5]) ## read elment at given index

for i in range(0,len(arr)):
    print(arr[i])   ## read elements of an array using loop

def check_value(arr,val):
    flag = True
    idx = 0
    for i in range(0,len(arr)):
        if arr[i] == val:
            flag = True 
            idx = i
            break
        else:
            flag = False
    if flag == True:
        print(f"{val} is present at {idx}th index")
    else:
        print(f"{val} is not present in the given array") 

print(check_value(arr,4))   
    

## UPDATE

