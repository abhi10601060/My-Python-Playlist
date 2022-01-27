class Node:
	def __init__(self,key):
		self.key=key
		self.next=None

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
head.next.next.next.next=head

def del_kth(head,k):
	if head==None:
		return None
	if head.next==head and k==1:
		return None

	if k==1:
		head.key=head.next.key
		head.next=head.next.next
		return head

	cur=head
	for i in range(1,k-1):
		cur=cur.next
	cur.next=cur.next.next
	return head

head=del_kth(head,2)

def print_list(head):
	if head==None:
		return None
	cur=head
	while cur.next!=head:
		print(cur.key)
		cur=cur.next
	print(cur.key)

print_list(head)