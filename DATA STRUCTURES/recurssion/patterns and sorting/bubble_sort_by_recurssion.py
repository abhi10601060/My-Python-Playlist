def recursive_bubble(arr,i,j):
	if i==0:
		return 
	if j<i:
		if arr[j]>arr[j+1]:
			arr[j],arr[j+1]=arr[j+1],arr[j]
		recursive_bubble(arr,i,j+1)
	recursive_bubble(arr,i-1,j)
arr=[266,89,5,4,7899,656,25,63,1,3,4]
recursive_bubble(arr,len(arr)-1,0)
print(arr)
