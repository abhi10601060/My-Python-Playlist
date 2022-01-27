arr = [7, 0, 1, 2]
start = 0
end = len(arr)-1
pivot = None
while start <= end:
    mid = (start+end)//2
    if mid == len(arr)-1 or arr[mid] > arr[mid+1]:
        pivot = mid
        break
    elif arr[mid] <= start:
        end = mid-1
    else:
        start = mid+1
print(pivot)
