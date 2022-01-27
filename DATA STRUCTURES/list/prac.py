arr=[1,2,3,4,5,6,9,10,11]
# x=9
# for i in arr:
#     if i>x :
#         arr.remove(i)
# print(arr)
# if len(arr)==0:
#     print(-1)
# else :
#     print(max(arr))
# y=10
# print(x,y)
# print(arr[::-1])


# def reverseArray(arr):
#     s=arr[::-1]
#     return print(s)
#     #code here
# reverseArray(arr)

A=[11,5,19,7,6]
N=5
if N%2==0:
    median=A[int(N/2)]
else :
    median= A[int((N-1)/2)]
print(median)