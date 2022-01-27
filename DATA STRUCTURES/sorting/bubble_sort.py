arr=[25,25,96,85,12,36,369,29256548]
N=len(arr)

for i in range(N-1):
    swapped=False
    for j in range(N-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            swapped=True
    if swapped==False:
        print(arr)
        break

