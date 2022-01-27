def search(arr,key,idx=0):
	ans=[]
	if idx==len(arr)-1:
		if arr[idx]==key:
			ans.append(idx)
			return ans
		else:
			return ans

	if arr[idx]==key:
		ans.append(idx)
		return ans+ search(arr,key ,idx+1)
	else:
		return search(arr,key,idx+1)


arr=[1,2,3,44,5,44,5,6]
print(search(arr,44))

