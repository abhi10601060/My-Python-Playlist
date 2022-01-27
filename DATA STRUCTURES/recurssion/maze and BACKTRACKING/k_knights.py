def Knights(arr,r,c,k):
	if k==0:
		display(arr)
		print( )
		return 
	if r==len(arr):
		return 

	if c==len(arr):
		Knights(arr,r+1,0,k)
		return

	if isSafe(arr,r,c):
		arr[r][c]=True
		Knights(arr,r,c+1,k-1)
		arr[r][c]=False

	Knights(arr,r,c+1,k)

def isSafe(arr,r,c):
	if isvalid(arr,r-2,c+1):
		if arr[r-2][c+1]:
			return False
	if isvalid(arr,r-2,c-1):
		if arr[r-2][c-1]:
			return False
	if isvalid(arr,r+2,c-1):
		if arr[r+2][c-1]:
			return False
	if isvalid(arr,r+2,c+1):
		if arr[r+2][c+1]:
			return False
	if isvalid(arr,r-1,c+2):
		if arr[r-1][c+2]:
			return False

	if isvalid(arr,r-1,c-2):
		if arr[r-1][c-2]:
			return False
	if isvalid(arr,r+1,c-2):
		if arr[r+1][c-2]:
			return False
	if isvalid(arr,r-1,c+2):
		if arr[r-1][c+2]:
			return False

	return True	


def isvalid(arr,r,c):
	if r>=0 and r<len(arr) and c>=0 and c< len(arr):
		return True
	else:
		return False


def display(arr):
	for x in arr:
		for y in x:
			if y==True:
				y="K"
			else:
				y="X"
			print(y,end=" ")
		print( )


arr=[[False,False,False,False],
	[False,False,False,False],
	[False,False,False,False],
	[False,False,False,False]]
Knights(arr,0,0,4)