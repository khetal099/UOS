diskArray=[10,50,9,802,907,56,4596,45,86,49,73,69,12,345,671,159,753,123,456,741,951,852,638]
arr=[12,10,8,6,4,3,2,1]
diskArrayRemovedElement = []
length=len(arr)
print("Initially Disk Array contents are",diskArray)
print("Initially Array contents are",arr)

flag=0
while(len(arr)>1):
    flag= 1
    print("Process needs inode")
    print("removing element",arr[-1])
    arr.pop()
    print("Array contents are",arr)
    
print("Remember inode is ",arr[0])
print("Searching for elements greater than remember inode in disk array")

temp=arr[0]
arr.clear()

for i in range(len(diskArray)):
    if length<=len(arr):
        break
    if(diskArray[i]>temp):
        diskArrayRemovedElement.append(diskArray[i])
        arr.append(diskArray[i])
        
arr.sort(reverse=True)
print("Array contents are",arr)
print("Index pointing to",arr[-1])
for i in range(len(diskArrayRemovedElement)):
    diskArray.remove(diskArrayRemovedElement[i])
    
diskArray.append(temp)
print("Disk Element contents are",diskArray)


        
