arr=[-1,2,-8,-10]
N=len(arr)
for i in range(N-1):
    minn=i
    for j in range(i+1,N):
        if arr[j]<arr[minn]:
            minn=j
    arr[minn],arr[i]=arr[i],arr[minn]
print(arr)