class Node :
	def __init__(self, val):

		self.val=val
		self.left=None
		self.right=None


root= Node(10)
root.left=Node(20)
root.left.left=Node(60)
root.left.left.right=Node(70)
root.left.left.right.left=Node(80)
root.right=Node(30)
root.right.left=Node(40)
root.right.right=Node(50)


def iterativePreorder(root):
	if(root==None):
		return []

	ans=[]
	st=[root]

	while(len(st)>0):
		cur=st.pop()
		ans.append(cur.val)

		if(cur.right != None):
			st.append(cur.right)
		if(cur.left!=None):
			st.append(cur.left)

	return ans

ans=iterativePreorder(root)
print(ans)
