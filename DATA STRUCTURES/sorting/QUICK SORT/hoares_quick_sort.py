def hoares_sort(arr,low,high):
	if low<high:
		pivot=hoares_partition(arr,low,high)
		hoares_sort(arr,low,pivot-1)
		hoares_sort(arr,pivot+1,high)
def hoares_partition(arr,low,high):
	pivot=arr[low]
	i=low
	j=high
	while i<j:
		while arr[i]<pivot:
			i+=1

		while arr[j]>pivot:
			j-=1
		if i==j:
			return j

		if i<j:
			arr[i],arr[j]=arr[j],arr[i]
	
	return j




arr=[5,1,1,2,0,0]

hoares_sort(arr,0,len(arr)-1)
print(arr)