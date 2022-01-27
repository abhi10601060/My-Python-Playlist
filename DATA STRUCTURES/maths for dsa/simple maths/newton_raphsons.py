def square_root_NRM(n):
	x=n 
	root=None
	while True:
		root=0.5*(x+(n/x))
		if abs(root-x)<0.5:
			return round(root,3) 
		x=root 
print(square_root_NRM(40))