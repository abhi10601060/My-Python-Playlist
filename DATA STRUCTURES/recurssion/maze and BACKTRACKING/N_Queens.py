def Queens(arr,r=0):
	if r==len(arr):
		display(arr)
		print( )
		return

	for c in range(len(arr)):
		if isSafe(arr,r,c):
			arr[r][c]=True 
			Queens(arr,r+1)
			arr[r][c]=False


def isSafe(arr,r,c):
	for i in range(r):
		if arr[i][c]==True:
			return False

	mxright=min(r,len(arr)-1-c)
	for i in range(1,mxright+1):
		if arr[r-i][c+i]==True:
			return False

	mxleft=min(r,c)
	for i in range(1,mxleft+1):
		if arr[r-i][c-i]==True:
			return False
	return True

def display(arr):
	for x in arr:
		for y in x:
			if y==True:
				y="Q"
			else:
				y="X"
			print(y,end=" ")
		print( )

arr=[[False,False,False,False],
	[False,False,False,False],
	[False,False,False,False],
	[False,False,False,False]]
(Queens(arr))


