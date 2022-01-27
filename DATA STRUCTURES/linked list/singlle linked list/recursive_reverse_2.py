


class node:
	def __init__(self,key):
		self.key=key
		self.next=None

head=node(10)
head.next=node(20)
head.next.next=node(30)
head.next.next.next=node(40)


def reverse(cur,pre=None):
	if cur==None:
		return pre

	next_node=cur.next
	cur.next=pre
	return reverse(next_node,cur)

head=reverse(head)

def printlist(head):
	cur=head
	while cur!=None:
		print(cur.key)
		cur=cur.next

printlist(head) 
