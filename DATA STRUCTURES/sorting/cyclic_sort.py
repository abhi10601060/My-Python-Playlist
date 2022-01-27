
# only useful for 1 to N or 0 to N-1 numbers 
# may be useful for range of continous numbers
def cyclic_sort(arr):
	i=0
	while i<len(arr):
		if arr[i]!=i+1:
			correct=arr[i]-1
			arr[correct],arr[i]=arr[i],arr[correct]
		else:
			i+=1
	return arr
ar=[1,3,5,8,2,6,4,7]
print(cyclic_sort(ar))