diskArray=[10,50,9,802,907,56,4596,45,86,49,73,69,12,345,671,159,753,123,456,741,951,852,638]
arr=[12,10,8,6,4,3,2,1]
print("Before process contents of both array are \n ",diskArray,"\n",arr)
length=len(arr)

sizeOfArray=10
print("Fix size of array full is 10 \n Size of given array is",length)
x=int(input("Enter an element to insert : "))

if(sizeOfArray == length):
    diskArray.append(x)
else:
    arr.append(x)
    
print("After Process succesfully content of both array is \n ",diskArray,"\n",arr)
