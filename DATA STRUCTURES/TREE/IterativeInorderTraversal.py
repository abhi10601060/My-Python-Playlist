class Node :
	def __init__(self, val):

		self.val=val
		self.left=None
		self.right=None


root= Node(10)
root.left=Node(20)
root.right=Node(30)
root.right.left=Node(40)
root.right.right=Node(50)


def iterativeInorder(root):
	if(root==None):
		return []

	ans=[]
	st=[]

	cur=root
	while (cur!=None):
		st.append(cur)
		cur=cur.left

	while(len(st)>0):
		cur=st.pop()
		ans.append(cur.val)
		cur=cur.right
		while (cur!=None):
			st.append(cur)
			cur=cur.left

	return ans


ans=iterativeInorder(root)
print(ans)