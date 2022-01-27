def maze_all_paths(arr,r=0,c=0,ans="",temp=[]):
	if r==len(arr)-1 and c==len(arr[0])-1:
		temp.append(ans)
		return
	if arr[r][c]==False:
		return
	arr[r][c]=False                             #to mark that cell is already followed... 

	if r>0:
		maze_all_paths(arr,r-1,c,ans+"U",temp)
	if c>0:
		maze_all_paths(arr,r,c-1,ans+"L",temp)
	if r<len(arr)-1:
		maze_all_paths(arr,r+1,c,ans+"D",temp)
	if c<len(arr[0])-1:
		maze_all_paths(arr,r,c+1,ans+"R",temp)
	arr[r][c]=True                               #backtracking...
	return temp
arr=[[True,True,True],[True,True,True],[True,True,True]]
print(maze_all_paths(arr))

# backtracking in this problem is basically making the matrix cell (True) as it is before the function call
# in this problem to avoid the stackoverflow we mark the current cell as false so in next call it does not take it in consideration...
# and by backtracking we make it again True for next possible call in that function....
