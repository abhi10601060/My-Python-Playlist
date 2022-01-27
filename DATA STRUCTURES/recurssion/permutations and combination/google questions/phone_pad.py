def phone_pad(digits,ans="",temp=[]):
	if digits=="":
		temp.append(ans)
		return
	digit=int(digits[0])
	for i in range(3*(digit-1),3*(digit)):
		char=chr(97+i)
		phone_pad(digits[1:],ans+char)
	return temp
print(phone_pad("12"))

