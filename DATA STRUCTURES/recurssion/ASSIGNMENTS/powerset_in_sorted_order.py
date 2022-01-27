def power_set(str):
	ans=[""]
	string=sorted(str)
	for x in string:
		for i in range (len(ans)):
			ans.append(ans[i]+x)
	ans.sort()
	return ans[1:]
str="abc"
print(power_set(str))