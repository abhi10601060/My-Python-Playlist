def balanced_paranthesis(str):

	if len(str)%2!=0:
		return False

	d={ "(":")","[":"]","{":"}"}

	data=["(","[","{"]

	temp=[]


	for i in range (len(str)):

		if str[i] in data:
			temp.append(str[i])
			continue

		if str[i]==d[temp.pop()]:
			continue

		else:
			return False

	if temp:
		return False

	else:
		return True



print(balanced_paranthesis("()"))