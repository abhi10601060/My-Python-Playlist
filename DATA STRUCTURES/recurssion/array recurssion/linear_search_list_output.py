def search(arr,key,idx=0,ans=[]):
	if arr[idx]==key:
		ans.append(idx)
	if idx==len(arr)-1:
		if len(ans)==0:
			return "not found :("
		else:
			return ans
	else:
		return search(arr,key,idx+1,ans)
arr=[1,2,3,44,5,44,5,6]
print(search(arr,44))