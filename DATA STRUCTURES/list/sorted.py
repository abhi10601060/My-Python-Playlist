def get_sort(l):
    if len(l)<=1:
        return print("sorted")
    a=l[0]
    b=None
    for x in l[1:]:
        if a<=x:
            a=x
            b=True
        else :
            b=False
            return print("not sorted")
    if b==True:
        return print("sorted")
k=[50,32,69]
get_sort(k)


a=list(reversed(sorted(k)))
print(a)
k.remove(1)