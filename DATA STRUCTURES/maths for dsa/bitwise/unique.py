def unique(arr):
	ans=arr[0]
	for x in arr[1:]:
		ans=ans^x
	return ans
print(unique([2,2,6,9,6,4,4,8,3,8,3]))