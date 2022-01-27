arr = [3,1]
x = 1
ans = -1
start = 0
end = len(arr)-1
pivot = 0
while start <= end:
    mid = (start+end)//2
    if mid == len(arr)-1 or arr[mid] > arr[mid+1]:
        pivot=mid
        break
    elif start >= arr[mid]:
        end = mid-1
    else:
        start = mid+1
print(pivot)

low = 0
high = pivot
while low <= high:
    mid = (low+high)//2
    if arr[mid] == x:
        ans = mid
        break
    elif x > arr[mid]:
        low = mid+1
    else:
        high = mid-1
else:
    low1 = pivot+1
    high1 = len(arr)-1
    while low1 <= high1:
        mid1 = (low1+high1)//2
        if arr[mid1] == x:
            ans = mid1
            break
        elif x > arr[mid1]:
            low1 = mid1+1
        else:
            high1 = mid1-1
print(ans)
