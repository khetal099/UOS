diskArray = [10,20,30,1,5,2,63,3,50,23,36,6,31,32,52,90,60,96,552,22,31,2566,34,69,15,236,2454,3665,14,24]
arr = [12,10,8,7,6,5,3,2,5,3]
print("Before process contents of both array are\n",diskArray,"\n",arr)
length = len(arr)

sizeOfArray = 10
print("Fix size of array to became full is 10 \nSize of given array is ",length)
x = int(input("Enter an element to insert "))

if(sizeOfArray == length):
    temp = arr[0]
    if(arr[0]<x):
        arr[0] = x
        diskArray.append(temp)
    else:
        diskArray.append(x)
    else:
        arr.append(x)

print("After process successfully executed content of both array is\n",diskArray,"\n",arr)
