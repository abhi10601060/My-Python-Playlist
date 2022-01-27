def linear(arr,key,i=0):
	if i==len(arr)-1:
		return "not found :("
	elif arr[i]==key:
		return i
	return linear(arr,key,i+1)
arr=[2,3,6,9,8,9,56,1,2,3,6,65]
print(linear(arr,12365))