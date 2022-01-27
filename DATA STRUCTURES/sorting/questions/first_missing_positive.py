def missing_positive(arr):
	n=len(arr)
	i=0
	while i<len(arr):
		if arr[i]!=i+1 and arr[i]>0 and arr[i]<=n:
			correct=arr[i]-1
			arr[correct],arr[i]=arr[i],arr[correct]
		else:
			i+=1
	return arr
ar=[4,2,-1,3]
print(missing_positive(ar))