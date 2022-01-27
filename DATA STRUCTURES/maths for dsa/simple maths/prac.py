def selection(arr):
    for i in range(len(arr)-1):
        min=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min]:
                min=j
        arr[min],arr[i]=arr[i],arr[min]
    return(arr)
arr=[1,2,3,6,5,9,8,7,4]


print(selection(arr))

