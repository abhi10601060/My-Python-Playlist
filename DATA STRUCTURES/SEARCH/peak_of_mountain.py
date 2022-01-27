arr=[0,1,0]

start=0
end=len(arr)-1
while start<=end:
    mid=(start+end)//2
    if arr[mid]<=arr[mid+1]:
        start=mid+1
    elif arr[mid]<arr[mid-1]:
        end=mid-1
    else:
        print(arr[mid])
        break
        
         
