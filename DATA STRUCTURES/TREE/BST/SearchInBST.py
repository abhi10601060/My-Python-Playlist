def search(self, node, x):
        #code here
    cur=node
        
    while(cur!=None):
        if (cur.data==x):
            return 1
        elif(x<cur.data):
            cur=cur.left
        else:
            cur=cur.right
            
    return 0           
                