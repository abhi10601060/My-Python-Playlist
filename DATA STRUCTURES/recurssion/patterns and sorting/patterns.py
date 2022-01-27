def triangle(n):
	if n==1:
		return "*"
	print("* "*n)
	return triangle(n-1)
print(triangle(4))