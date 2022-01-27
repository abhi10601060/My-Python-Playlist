def maze_path(r,c,ans="",temp=[]):
	if r>0 and c>0:
		if r==1 and c==1:
			temp.append(ans)
			return
		maze_path(r-1,c-1,ans+"d",temp)
		maze_path(r-1,c,ans+"D",temp)
		maze_path(r,c-1,ans+"R",temp)
		return temp



print(maze_path(3,3))