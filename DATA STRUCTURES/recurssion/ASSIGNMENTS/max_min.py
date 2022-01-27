def Mm(arr,max1,min1):
	if len(arr)==1:
		print(max1)
		print(min1)
		return 

	if arr[0]>max1:
		Mm(arr[1:],arr[0],min1)
	if arr[0]<min1:
		Mm(arr[1:],max1,arr[0])
arr=[0,2,55,65,51,22,-63,32]
print(Mm(arr,0,0))
