def permutation(str,ans="",temp=[]):
	if str=="":
		print(ans)
		return 
	ch=str[0]
	for i in range(len(ans)):
		first=ans[0:i]
		last=ans[i:]
		permutation(str[1:],first+ch+last,)
	permutation(str[1:],ans+ch)
str="abc"
(permutation(str))
