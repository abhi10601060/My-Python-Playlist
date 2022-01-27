def dice(n,ans="",temp=[]):
	if n==0:

		temp.append(ans)
		return 

	for i in range(1,n+1):
		num=str(i)
		dice(n-i,ans+num,temp)
	return temp


print(dice(4))