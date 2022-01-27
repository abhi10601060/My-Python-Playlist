def print_prime(n):
	prime=[]
	for i in range (2,n+1):
		c=2
		while c*c<=i:
			if i%c==0:
				break
			c+=1
		else :
			prime.append(i)
	return prime
			
print(print_prime(40))