# def get_sum(l):
#     a=sum(l)
#     return print("average :",a/len(l))
# l=[23,45,12,63]
# get_sum(l)


# def sep(l):
#     even=[]
#     odd=[]
#     for i in l:
#         if i%2==0:
#             even.append(i)
#         else:
#             odd.append(i)
#     return print(even) , print(odd)
# l=[12,25,66,445,3,4565,3,56,2]
# sep (l)


def smaller(l,x):
    s=[]
    for i in l:
        if i<x:
            s.append(i)
    return print(s)

l=[23,45,12,63]
smaller(l,40)