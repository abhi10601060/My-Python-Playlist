def subsequence(str):
	if str=="":
		return [" "]
	temp=subsequence(str[1:])
	res=[" "]*2* (len(temp))

	k=0
	for i in range(len(temp)):
		res[k]=temp[i]
		k+=1
	for i in range(len(temp)):
		res[k]=str[0]+temp[i]
		k+=1
	return res

str="abhi"
print(subsequence(str))
