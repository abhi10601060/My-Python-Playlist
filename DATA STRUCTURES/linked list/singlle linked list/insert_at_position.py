class node:
	def __init__(self,key):
		self.key=key
		self.next=None

head=node(10)
head.next=node(20)
head.next.next=node(30)
head.next.next.next=node(40)

def insert_at_position(head,pos,key):
	temp=node(key)
	if pos==1:
		temp.next=head
		return temp
	cur=head
	for i in range(1,pos-1):
		cur=cur.next
		if cur==None:
			return head
	temp.next=cur.next
	cur.next=temp
	return head
head=insert_at_position(head,5,15)


def printlist(head):
	cur=head
	while cur!=None:
		print(cur.key)
		cur=cur.next

printlist(head) 
