def uppercase(s,c=0):
	if s[c].isupper():
		return s[c]
	else:
		return uppercase(s,c+1)
print(uppercase("sdhuaRfgkjgH jfaK"))
