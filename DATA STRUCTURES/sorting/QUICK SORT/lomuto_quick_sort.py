def lomuto_sort(arr,low,high):
	if low<high:
		pivot=lomuto_partition(arr,low,high)
		lomuto_sort(arr,low,pivot-1)
		lomuto_sort(arr,pivot+1,high)

def lomuto_partition(arr,low,high):
	pivot=arr[high]
	i=low-1
	j=low
	while j<high:
		if arr[j]<pivot:
			i+=1
			arr[j],arr[i]=arr[i],arr[j]
		j+=1
	
	arr[high],arr[i+1]=arr[i+1],arr[high]
	return i+1

arr=[1,1]
lomuto_sort(arr,0,len(arr)-1)
print(arr)