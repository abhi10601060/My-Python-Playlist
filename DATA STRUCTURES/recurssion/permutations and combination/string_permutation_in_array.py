def permutation_in_array(str,ans="",temp=[]):
	if str=="":
		temp.append(ans)
		return
	ch=str[0]
	for i in range (len(ans)):
		first=ans[:i]
		last=ans[i:]
		permutation_in_array(str[1:],first+ch+last)
		
	
	
	permutation_in_array(str[1:],ans+ch)
	return temp



str="abcd"
print(permutation_in_array(str))