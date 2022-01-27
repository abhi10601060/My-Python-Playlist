def missing(arr):
	n=len(arr)
	ans=[]
	for i in range(n):
		if arr[i]!=i+1:
			correct=arr[i]-1
			arr[i],arr[correct]=arr[correct],arr[i]
	print(arr)
	for i in range(n):
		if arr[i]!=i+1:
			ans.append(i+1)
	return ans
ar=[4,3,2,7,8,2,3,1]
print(missing(ar))