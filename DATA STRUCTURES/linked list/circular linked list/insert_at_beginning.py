class Node:
	def __init__(self,key):
		self.key=key
		self.next=None

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
head.next.next.next.next=head

def insert_begining(head,key):
	temp=Node(key)
	if head==None:
		temp.next=temp
		return temp

	cur=head
	while cur.next!=head:
		cur=cur.next
	cur.next=temp
	temp.next=head
	return temp

head=insert_begining(head,5)

def print_list(head):
	if head==None:
		return None
	cur=head
	while cur.next!=head:
		print(cur.key)
		cur=cur.next
	print(cur.key)

# print_list(head)

head1=None
head1=insert_begining(head1,10)
head1=insert_begining(head1,2)
print_list(head1)


