def tri(arr):
	if len(arr)==1:
		return
	ans=[]
	for i in range(1,len(arr)):
		ans.append(arr[i]+arr[i-1])
	tri(ans)
	print(ans)


tri([1,2,3,4,5])