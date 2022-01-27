# def subsequence(str):
# 	ans=[" "]
# 	for i in range(len(str)):
# 		ans.append(str[i])
# 		if i==len(str)-1:
# 			return ans
# 		for j in range(i+1,len(str)):
# 			if j==i+1:
# 				ans.append(str[i]+str[j])
# 				continue
# 			ans.append(str[i]+str[j])
# 			ans.append(str[i:j+1])
# str="abhi"
# print(sorted(subsequence(str)))


def subsequence1(str):
	ans=[" "]

	for x in str:
		for i in range(len(ans)):
			if i ==0:
				ans.append(x)
				continue
			ans.append(ans[i]+x)
	return ans
str="abhi"
print(sorted(subsequence1(str)))










