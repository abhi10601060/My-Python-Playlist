def skip(str,ans="",i=0):

	if i==len(str):
		print(ans)
		return
	ch=str[i]
	if ch!="a":
		skip(str,ans+ch,i+1)
	else:
		skip(str,ans,i+1)
str="sndnadfad"
(skip(str))
