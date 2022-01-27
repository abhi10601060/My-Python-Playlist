class Node:
	def __init__(self,key):
		self.key=key
		self.next=None

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
head.next.next.next.next=head


def del_head(head):
	if head==None:
		return None 
	if head.next==head:
		return None

	cur=head
	while cur.next!=head:
		cur=cur.next
	cur.next=head.next
	return cur.next

head=del_head(head)

def print_list(head):
	if head==None:
		return None
	cur=head
	while cur.next!=head:
		print(cur.key)
		cur=cur.next
	print(cur.key)

# print_list(head)

head1=Node(10)
head1.next=head1
head1=del_head(head1)
print_list(head1)