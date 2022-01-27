def get_odd(l):
    for x in l:
        count=0
        for j in l:
            if x==j:
                count+=1
        if count%2!=0:
            return print(x)
l=[10,30,30,10,20,20,10,30,30]
get_odd(l)