def selection(arr,i,j):
	if i==len(arr)-2:
		return
	if arr[j]<arr[i]:
		arr[j],arr[i]=arr[i],arr[j]
	if j==len(arr)-1:
		selection(arr,i+1,j+1)

	selection(arr,i,j+1)
arr=[266,89,5,4,7899,656,25,63,1,3,4]
selection(arr,0,1)
print(arr)