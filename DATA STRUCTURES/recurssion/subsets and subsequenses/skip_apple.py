def skip(str,i=0):
	if i>=len(str):
		return 
	temp=str[i:]
	ch=str[i]
	if temp.startswith("apple"):
		return skip(str,i+5)

	else:
		return ch+ skip(str,i+1)
str="ajdajdappsadg"
print(skip(str))


