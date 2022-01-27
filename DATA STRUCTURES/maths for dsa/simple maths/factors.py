def factors(n):
	asc=[]
	dec=[]
	for i in range (1,int(n**(0.5))+1):
		if n%i==0:
			asc.append(i)
			dec.append(int(n/i))
	return asc+dec[::-1]
print(factors(20))