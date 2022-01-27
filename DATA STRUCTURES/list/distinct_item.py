l=[20,30,62,10,30,20,20,10,30,10,30]
ans=1
for i in range(1,len(l)):
        if l[i] not in l[:i]:
            ans+=1 
          
print(ans)



