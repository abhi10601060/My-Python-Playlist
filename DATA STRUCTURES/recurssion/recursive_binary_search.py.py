def binary_search(arr,target,start,end):
    if start>end:
        return -1
    mid=(start+end)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]<target:
        return binary_search(arr,target,mid+1,end)
    else:
        return binary_search(arr,target,start,end=mid-1)
l=[1,2,3,6,89,789,58236]
x=789
print(binary_search(l,x,0,len(l)-1))