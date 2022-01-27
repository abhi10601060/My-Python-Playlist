def merge_sort(arr):
	if len(arr)<=1:
		return  
	mid=len(arr)//2
	lef=arr[:mid]
	righ=arr[mid:]
	merge_sort(lef)
	merge_sort(righ)
	merge(lef,righ,arr)
def merge(left,right,arr):
	i=j=k=0
	while i<len(left) and j<len(right):
		if left[i]<=right[j]:
			arr[k]=left[i]
			i+=1
			k+=1
		else:
			arr[k]=right[j]
			j+=1
			k+=1
	while i<len(left):
		arr[k]=left[i]
		i+=1
		k+=1
	while j<len(right):
		arr[k]=right[j]
		j+=1
		k+=1
arr=[2,3,6,5,4]
merge_sort(arr)
print(arr)
