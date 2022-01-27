def merge_sort(arr):
	if len(arr)==1:
		return arr
	mid=len(arr)//2
	left=arr[0:mid]
	right=arr[mid:]
	left=merge_sort(left)
	right=merge_sort(right)
	return merge(left,right)
def merge(left, right):
	ans=[]
	i=0
	j=0
	while i<len(left) and j<len(right):
		if left[i]<=right[j]:
			ans.append(left[i])
			i+=1
		else:
			ans.append(right[j])
			j+=1
	if i<len(left):
		ans+=left[i:]
	if j<len(right):
		ans+=right[j:]
	return ans
arr=[5,6,4,2,3]
print(merge_sort(arr))