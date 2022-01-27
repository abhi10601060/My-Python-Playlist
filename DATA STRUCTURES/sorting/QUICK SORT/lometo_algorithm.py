# in lometo we use two pointers and pivot
# pivot is always last element
# and two pointers will be alternate starts from -1 and 0th element as i and j  resp.
# we traverse j through whole list till before pivot (last element - 1)
# if j finds an element which is smaleer than pivot then i+=1 and swap jth element with ith element
# when loop ends replace pivot with i+1th element
# so all the left element from pivot will be less than pivot and right be greater than pivot



def lometo(arr,low,high):
	pivot=arr[high]
	i=low-1
	j=low
	while j<high:
		if arr[j]<pivot:
			i+=1
			arr[i],arr[j]=arr[j],arr[i]
		j+=1
	arr[i+1],arr[high]=arr[high],arr[i+1]
	return arr
arr=[2,6,9,8,4,5,6]
print(lometo(arr,0,len(arr)-1))