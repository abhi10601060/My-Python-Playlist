def missing_no(arr):
	n=len(arr)
	i=0
	while i<len(arr):
		if arr[i]!=i and arr[i]<n:
			correct=arr[i]
			arr[correct],arr[i]=arr[i],arr[correct]
		else:
			i+=1	
	for i in range(n):
		if i!=arr[i]:
			return i
	else:
		return n
ar=[7,2,3,4,1,2,3,8]
print(missing_no(ar))