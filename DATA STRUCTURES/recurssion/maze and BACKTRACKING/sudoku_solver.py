def is_empty(arr):
	for i in range(9):
		for j in range(9):
			if arr[i][j]==0:
				return i,j
	return None,None


def sudoku_solver(arr):
	r,c=is_empty(arr)
	if r==None:
		display(arr)
		return 
	for guess in range(1,10):
		if is_safe(arr,r,c,guess):
			arr[r][c]=guess
			if sudoku_solver(arr):
				return True
		arr[r][c]=0
	return False
def is_safe(arr,r,c,guess):

	for i in range(9):
		if arr[i][c]==guess:
			return False

	for i in range(9):
		if arr[r][i]==guess:
			return False

	rowstart=r-r%3
	colstart=c-c%3
	for i in range (3):
		for j in range (3):
			if arr[rowstart+i][colstart+j]==guess:
				return False
	return True


def display(arr):
	for x in arr:
		for y in x:
			print(y,end=" ")
		print( )


arr=[
                [3, 0, 6, 5, 0, 8, 4, 0, 0],
                [5, 2, 0, 0, 0, 0, 0, 0, 0],
                [0, 8, 7, 0, 0, 0, 0, 3, 1],
                [0, 0, 3, 0, 1, 0, 0, 8, 0],
                [9, 0, 0, 8, 6, 3, 0, 0, 5],
                [0, 5, 0, 0, 9, 0, 6, 0, 0],
                [1, 3, 0, 0, 0, 0, 2, 5, 0],
                [0, 0, 0, 0, 0, 0, 0, 7, 4],
                [0, 0, 5, 2, 0, 6, 3, 0, 0]
        ]
sudoku_solver(arr)
