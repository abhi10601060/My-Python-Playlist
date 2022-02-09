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

def search(root,key):
	if root==None:
		return False

	if(root.val==key):
		return True

	return search(root.left,key) or search(root.right,key)

def optimisedSearch (root, key):
	if(root==None):
		return False

	elif(root.val==key):
		return True

	elif(optimisedSearch(root.left,key)==True):
		return True

	elif (optimisedSearch(root.right,key)==True):
		return True

	return False

def optimisedSearch2 (root, key):
	if(root==None):
		return False

	elif(root.val==key):
		return True

	elif(optimisedSearch2(root.left,key)==True):
		return True

	else:
	    return optimisedSearch2(root.right,key)
		

print(optimisedSearch2(root,80))