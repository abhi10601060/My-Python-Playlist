def count(n,c=0):
	if n==0:
		return c  
	if n%10==0:
		return count(n//10,c+1)
	else:
		return count(n//10,c)

print(count(10000))