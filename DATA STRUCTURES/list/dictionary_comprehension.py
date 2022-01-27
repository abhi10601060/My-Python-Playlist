l=[25,1,3,8,65,3,2,9,8,7,4,5,6]

d1={x:x**2 for x in l }
print(d1)

l1=["ghf","geeks","hi"]
l2=[1,2,3]
d2={l1[i]:l2[2] for i in range(len(l1))}
print(d2)
d5=dict(zip(l1,l2))
print(d5)

d3={1:2,5:4,6:7}
d4={v:k for (k,v) in d3.items()}
print(d4)