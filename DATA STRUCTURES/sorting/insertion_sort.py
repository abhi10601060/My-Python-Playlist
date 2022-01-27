arr=[5,6,2,3,4,1,8]
N=len(arr)
for i in range(N-1):
    for j in range (i+1,0,-1):
        if arr[j]<arr[j-1]:
            arr[j],arr[j-1]=arr[j-1],arr[j]
        else:
            break
print (arr)