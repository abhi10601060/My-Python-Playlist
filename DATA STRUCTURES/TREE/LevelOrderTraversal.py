from collections import deque

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


def bfs(root):
	if(root==None):
		return []

	ans=[]
	q=deque()
	q.append(root)

	while(len(q)>0):
		level=len(q)
		lst=[]

		for i in range(level):
			cur=q.popleft()
			lst.append(cur.val)

			if cur.left!=None:
				q.append(cur.left)
			if cur.right!=None:
				q.append(cur.right)	

		ans.append(lst)

	return ans


ans=bfs(root)
print(ans)