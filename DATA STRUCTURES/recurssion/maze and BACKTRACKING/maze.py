def maze(r,c):
	if r==1 or c==1:
		return 1
	return maze(r-1,c)+maze(r,c-1)
print(maze(3,3))