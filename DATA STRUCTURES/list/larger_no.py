l=[1,2,3,65,4,8,9,5,6,2,3]
for x in l:
    for y in l:
        if y>x:
            break
    else:
        print(x)

l1=l[0]
for i in range(1,len(l)):
    if l[i]>l1:
        l1=l[i]
print(l1)

print(max(l))


a=max(10,20)
print (a)