l=[0,1,2,3,4,5,6,7,8,9]
N=len(l)
x=50
low=0
high=N-1
while low<=high:
    mid=(low+high)//2
    if l[mid]==x:
        print(1)
        break
    elif x>l[mid]:
        low=mid+1
    else:
        high=mid-1
else:
    print(-1)


