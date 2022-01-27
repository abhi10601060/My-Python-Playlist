def subsequence(str,ans=""):
	if str=="":
		print(ans)
		return
	ch=str[0]

	subsequence(str[1:],ans+ch)
	subsequence(str[1:],ans)
str="abc"
subsequence(str)