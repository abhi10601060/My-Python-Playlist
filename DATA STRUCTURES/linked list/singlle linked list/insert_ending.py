class node:
	def __init__(self,key):
		self.key=key
		self.next=None

head=node(10)
head.next=node(20)
head.next.next=node(30)
head.next.next.next=node(40)

def insert_end(head,key):
	if head==None:
		return node(key)
	cur=head
	while cur.next!=None:
		cur=cur.next
	cur.next=node(key)
	return head

head=insert_end(head,50)

def printlist(head):
	cur=head
	while cur!=None:
		print(cur.key)
		cur=cur.next

printlist(head) 