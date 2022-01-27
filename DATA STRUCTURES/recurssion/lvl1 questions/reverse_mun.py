def reverse(n,b):
	if n<10:
		return n
	a=(n%10)
	
	return a*(10**(b-1))+reverse(n//10,b-1)

print(reverse(1000053,7))