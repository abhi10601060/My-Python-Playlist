def is_sorted(arr,idx=0):
	if idx==len(arr)-1:
		return True
	return arr[idx]<arr[idx+1] and is_sorted(arr,idx+1)
ar=[3,5]
print(is_sorted(ar,0))