def insert(root, Key):
    # code here
    if (root==None):
        return Node(Key)
    
    cur = root 
    pre=None
    
    while (cur!=None):
        if(cur.data==Key):
            return root
        elif(Key>cur.data):
            pre=cur
            cur=cur.right
        else:
            pre=cur
            cur=cur.left
        
    
    if(Key>pre.data):
        pre.right=Node(Key)
    else:
        pre.left=Node(Key)
    
    return root


def recursiveInsert(root,Key):
    if(root==None):
        return Node(Key)

    if(root.data==Key):
        return root

    elif(Key>root.data):
        root.right=recursiveInsert(root.right,Key)
    else:
        root.left=recursiveInsert(root.left,Key)

    return root