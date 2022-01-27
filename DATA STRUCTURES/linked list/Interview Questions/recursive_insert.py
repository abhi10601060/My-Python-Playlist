class node:
	def __init__(self,key):
		self.key=key
		self.next=None

head=node(10)
head.next=node(20)
head.next.next=node(30)
head.next.next.next=node(40)

def rec_insert(head,pos,key):
	if pos==1:
		 temp=node(key)
		 temp.next=head
		 return temp
	next_node=rec_insert(head.next,pos-1,key)
	head.next=next_node
	return head


head=rec_insert(head,1,9)

def printlist(head):
	cur=head
	while cur!=None:
		print(cur.key)
		cur=cur.next

printlist(head) 
