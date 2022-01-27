# the matrix in this form is sorted but not strictly sorted....
# here the matrix sorted in row and column wise....
# complexity is O(n)


def TwoD_search(arr,target):
	r=0
	c=len(arr[0])-1
	while r<len(arr) and c>=0:
		 if arr[r][c]==target:
		 	return [r,c]
		 if arr[r][c]>target:
		 	c=c-1
		 if arr[r][c]<target:
		 	r=r+1
	return  False

arr=[[10,15,20],[30,35,42],[47,48,59]]
print(TwoD_search(arr,48))

