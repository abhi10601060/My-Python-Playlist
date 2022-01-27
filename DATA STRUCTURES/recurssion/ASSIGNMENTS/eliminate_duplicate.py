def eliminate(str,ans=""):
	if str=="":
		return ans
	ch=str[0]
	if ans.endswith(ch):
		return eliminate(str[1:],ans)
	else:
		return eliminate(str[1:],ans+ch)
str="geeeekforgeeeeeks"
print(eliminate(str))