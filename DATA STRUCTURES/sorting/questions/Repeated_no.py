def repeated(arr):
	n=len(arr)
	for  i in range(n):
		if arr[i]!=i+1:
			correct=arr[i]-1
			arr[i],arr[correct]=arr[correct],arr[i]
	for i in range(n):
		if arr[i]!=i+1:
			return arr[i]
ar=[1,2,2]
print(repeated(ar))