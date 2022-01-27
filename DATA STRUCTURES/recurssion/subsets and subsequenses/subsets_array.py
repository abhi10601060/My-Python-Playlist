def subset(arr):
	
	ans=[[]]
	for x in arr:
		for i in range(len(ans)):
			ans.append(ans[i]+[x])
	return ans
arr=[1,2,3]
print(subset(arr))