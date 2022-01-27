# either devide by 2 else -1
def steps(n,c=0):
	if n==0:
		return c 
	if n%2==0:
		return steps(n/2,c+1)
	else:
		return steps(n-1,c+1)
print(steps(8))