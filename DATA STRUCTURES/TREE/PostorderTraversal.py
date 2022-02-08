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
# root.left.right=Node(60)


def postorder(root ,ans):
	if(root==None):
		return ans

	postorder(root.left,ans)
	postorder(root.right,ans)
	ans.append(root.val)

	return ans

list=postorder(root,[])
print(list)
