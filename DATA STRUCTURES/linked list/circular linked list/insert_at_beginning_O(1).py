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

	temp.next=head.next
	head.next=temp
	head.key,temp.key=temp.key,head.key
	return head

head=insert_begining(head,5)
head=insert_begining(head,2)

def print_list(head):
	if head==None:
		return None
	cur=head
	while cur.next!=head:
		print(cur.key)
		cur=cur.next
	print(cur.key)

print_list(head)

head1=None
head1=insert_begining(head1,10)
head1=insert_begining(head1,2)
# print_list(head1)


