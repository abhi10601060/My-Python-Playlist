def ith_bit(n,i):
	return n&(1<<(i-1))
print(ith_bit(1011011010,7))