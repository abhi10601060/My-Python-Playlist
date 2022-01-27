txt=input("enter the file : ")
pat=input("enter the word : ")
pos=txt.find(pat)
while pos>=0:
    print(pos)
    pos=txt.find(pat,pos+1)