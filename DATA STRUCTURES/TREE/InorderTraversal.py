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


def inorder(root ,ans):
	if(root==None):
		return ans

	inorder(root.left,ans)
	ans.append(root.val)
	inorder(root.right,ans)

	return ans

list=inorder(root,[])
print(list)
