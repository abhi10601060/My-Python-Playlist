s1=input("enter string : ")
s2=input("enter string : ")
s1l=[]
s2l=[]
for x in s1:
    s1l.append(x)
for y in s2:
    s2l.append(y)
if s1l.sort()==s2l.sort():
    print("yes")
else:
    print ("no")