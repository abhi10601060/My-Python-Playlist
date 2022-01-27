class Node:
	def __init__(self,key):
		self.key=key
		self.next=None

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
tail=head.next.next.next
tail.next=head

def print_list(head):
	if head==None:
		return None
	cur=head
	while cur.next!=head:
		print(cur.key)
		cur=cur.next
	print(cur.key)

print_list(head)