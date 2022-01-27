class node:
	def __init__(self,key):
		self.key=key
		self.next=None

head=node(10)
head.next=node(20)
head.next.next=node(30)
head.next.next.next=node(40)

def del_last(head):
	if head == None:
		return None
	cur=head
	if cur.next==None:
		return None
	while cur.next.next!=None:
		cur=cur.next
	cur.next=None
	return head

head=del_last(head)


def printlist(head):
	cur=head
	while cur!=None:
		print(cur.key)
		cur=cur.next

printlist(head) 