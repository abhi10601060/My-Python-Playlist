class node:
	def __init__(self,key):
		self.key=key
		self.next=None

head=node(10)
head.next=node(20)
head.next.next=node(30)
head.next.next.next=node(40)

def reverse(head):
	cur=head
	pre=None
	while cur!=None:
		next_node=cur.next
		cur.next=pre
		pre=cur
		cur=next_node
	return pre 

head=reverse(head)


def printlist(head):
	cur=head
	while cur!=None:
		print(cur.key)
		cur=cur.next

printlist(head) 
	
