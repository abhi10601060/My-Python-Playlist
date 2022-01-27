def square_root(n,p):
	start=0
	end=n 
	tmp=0
	while start<=end:
		mid=start+(end-start)//2
		if mid*mid==n:
			tmp=mid
			break 
		elif mid*mid>n:
			end=mid-1
		else:
			start=mid+1
	else:
		tmp=end

	incr=0.1
	for i in range(p):
		while tmp*tmp<=n:
			tmp+=incr

		tmp-=incr
		incr/=10
	return round(tmp,3)

print(square_root(60,3))
