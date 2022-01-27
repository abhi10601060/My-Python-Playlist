class node:
	def __init__(self,key):
		self.key=key
		self.next=None

head=node(10)
head.next=node(20)
head.next.next=node(30)
head.next.next.next=node(40)

def del_head(head):
	if head==None:
		return None
	return head.next

head=del_head(head)


def printlist(head):
	cur=head
	while cur!=None:
		print(cur.key)
		cur=cur.next

printlist(head) 
