l=[1,2,3,5,6,89,2,3,2]
larg=l[0]
slarg=l[0]
for x in l[1:]:
    if x>larg:
        larg=x
        slarge=larg
        break
    elif x==larg:
        larg=larg
    elif x<larg and x>slarg:
            slarg=x
print(slarg)

