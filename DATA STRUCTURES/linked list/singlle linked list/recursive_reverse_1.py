class node:
	def __init__(self,key):
		self.key=key
		self.next=None

head=node(10)
head.next=node(20)
head.next.next=node(30)
head.next.next.next=node(40)

def reverse(head):
	if head==None:
		return None
	if head.next==None:
		return head

	next_head=reverse(head.next)

	tail=head.next
	tail.next=head
	head.next=None
	return next_head

head=reverse(head)

def printlist(head):
	cur=head
	while cur!=None:
		print(cur.key)
		cur=cur.next

printlist(head) 
	
