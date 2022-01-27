def prnt(n):
    if n==0:
        return
    print(n)
    
    prnt(n-1)
    print(n)
print(prnt(5))