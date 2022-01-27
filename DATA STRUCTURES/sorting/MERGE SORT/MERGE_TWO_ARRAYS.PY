def merge(arr1,arr2):
	ans=[]
	i=0
	j=0
	while i<len(arr1) and j<len(arr2):
		if arr1[i]<arr2[j]:
			ans.append(arr1[i])
			i+=1
		elif arr2[j]<arr1[i]:
			ans.append(arr2[j])
			j+=1
	if i== len(arr1):
		ans=ans+arr2[j:]
	if j==len(arr2):
		ans=ans+arr1[i:]
	return ans
arr1=[3,5,7]
arr2=[4,6,8]
print (merge(arr1,arr2))