l=[0,1,2,3,4,5,5,5,5,6,7,8,9,92,5656,9999,789999]
N=len(l)
x=789999
low=0
high=N-1
while low<=high:
    mid=(low+high)//2
    if x>l[mid]:
        low=mid+1
    elif x<l[mid]:
        high=mid-1
    elif l[mid]==x:
        if mid==N-1 or l[mid+1]!=x:
            print(mid)
            break
        else:
            low=mid+1
else:
    print(-1)