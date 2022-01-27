l=[0,1,2,3,5,5,5,6,7,8,9]
N=len(l)
x=5
low=0
high=N-1
while low<=high:
    mid=(low+high)//2
    if x>l[mid]:
        low=mid+1
    elif x<l[mid]:
        high=mid-1
    else:
        if mid==0 or l[mid-1]!=x:
            print(mid)
            break
        else:
            high=mid-1
        
else:
    print(-1)