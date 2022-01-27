# in this algo we take two pointers both at the extreme end elements of the array and one pivot at the middle element of the array
# pivot can be any element but middle is more prefered
# let i is first pointer at first element and j be the second pointer at last element 
# move both the pointers towards each other till its crosses
# between traversal if ith element founds greater than pivot element loop breaks ehen j traversal start if it found smaller element than oivot element then j loop breaks 
# after finding those elements swap both and again both pointers move till they cross each other


def hoares(arr,low,high):
	pivot=arr[low]
	i=low
	j=high
	while i<=j:

		while arr[i]<pivot:
			i+=1

		while arr[j]>pivot:
			j-=1

		if i>=j:
			break
		arr[i],arr[j]=arr[j],arr[i]
			
	print(arr)

	return j+1

arr=[2,3,4,1,5,6]
print(hoares(arr,0,len(arr)-1))