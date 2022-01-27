class node:
	def __init__(self,key):
		self.key=key
		self.next=None

head=node(10)
head.next=node(20)
head.next.next=node(30)
head.next.next.next=node(40)

def insert_sorted(head,key):
	temp=node(key)
	if key<head.key:
		temp.next=head
		return temp
	if head==None:
		return temp
	cur=head
	while cur.next!=None and cur.next.key<key:
		cur=cur.next
	temp.next=cur.next
	cur.next=temp
	return head

head=insert_sorted(head,25)

def printlist(head):
	cur=head
	while cur!=None:
		print(cur.key)
		cur=cur.next

printlist(head) 
	

