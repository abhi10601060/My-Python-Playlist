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


def height(root,count=0):
	if(root==None):
		return count

	ls=height(root.left,count+1)
	rs=height(root.right,count+1)

	return max(ls,rs)


def height2 (root):
	if(root==None):
		return 0

	ls=height2(root.left)
	rs=height2(root.right)

	return max(ls,rs)+1


# ans=height(root)

ans=height2(root)

print(ans)
