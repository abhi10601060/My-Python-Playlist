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



def size(root):
	if(root==None):
		return 0
	else:
		ls=size(root.left)
		rs=size(root.right)

		return ls + rs + 1

ans=size(root)
print(ans)