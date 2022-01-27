l=[12,56,878,544,6,2,3,87,12,56,3]

s1={x**2 for x in l}
print (s1)

s2={x for x in l if x%2==0}
s3={x for x in l if x%2!=0}
print(s2)
print(s3)