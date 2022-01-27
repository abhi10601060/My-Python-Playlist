def prnt(n):
	if n==1:
		return 1
	
	prnt(n-1)
	print(n-1)
print(prnt(5))