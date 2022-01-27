def missing(arr):
	n=len(arr)
	ans=[]
	for i in range (n):
		for j in range (n-i-1):
			if arr[j]>arr[j+1]:
				arr[j],arr[j+1]=arr[j+1],arr[j]
	for i in range(n):
		if arr[i]!=i+1:
			ans.append(i+1)
	return ans
ar=[7,2,3,4,1,2,3,8]
print(missing(ar))
