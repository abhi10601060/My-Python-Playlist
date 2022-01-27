class Node:
	def __init__(self,key):
		self.key=key
		self.next=None

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
head.next.next.next.next=head

def insert_end(head,key):
	temp=Node(key)
	if head==None:
		temp.next=temp
		return temp

	cur=head
	while cur.next!=head:
		cur=cur.next
	cur.next=temp
	temp.next=head
	return head

head=insert_end(head,50)


def print_list(head):
	if head==None:
		return None
	cur=head
	while cur.next!=head:
		print(cur.key)
		cur=cur.next
	print(cur.key)

print_list(head)

