def get_sum(n):
	if n<10:
		return n 
	return n%10+get_sum(n//10)
print(get_sum(4525))