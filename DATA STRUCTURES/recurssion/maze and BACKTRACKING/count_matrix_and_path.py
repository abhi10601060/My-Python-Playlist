def count_path(arr,r=0,c=0,ans="",count=1):

	if r==len(arr)-1 and c==len(arr[0])-1:
		arr[r][c]=count
		for x in arr:
			for y in x:
				print(y,end=" ")
			print()
		print(ans)
		return
	if arr[r][c]!=0:
		return
	arr[r][c]=count                          #to mark that cell is already followed... 

	if r>0:
		count_path(arr,r-1,c,ans+"U",count+1)
	if c>0:
		count_path(arr,r,c-1,ans+"L",count+1)
	if r<len(arr)-1:
		count_path(arr,r+1,c,ans+"D",count+1)
	if c<len(arr[0])-1:
		count_path(arr,r,c+1,ans+"R",count+1)
	arr[r][c]=0                            #backtracking...
	
arr=[[0,0,0],
     [0,0,0],
     [0,0,0]]
count_path(arr)
