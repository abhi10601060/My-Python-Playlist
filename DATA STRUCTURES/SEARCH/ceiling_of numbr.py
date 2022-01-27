l=[2,3,6,8,9,15,16,18,19]
x=9

low=0
high=len(l)-1
while low<=high:
    mid=(low+high)//2
    # if l[mid]==x:
    #     print(l[mid])
        # break
    if x>l[mid]:
        low=mid+1
    elif x<l[mid]:
        high=mid-1
else:
    print(l[low])