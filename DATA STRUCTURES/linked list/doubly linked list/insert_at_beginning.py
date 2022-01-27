class Node:
	def __init__(self,key):
		self.key=key
		self.pre=None
		self.next=None

head=Node(10)
temp1=Node(20)
temp2=Node(30)
head.next=temp1
temp1.next=temp2
temp1.pre=head
temp2.pre=temp1

head1=None

def _insert_beginning(head,key):
	temp=Node(key)
	if head==None:
		temp.next=head
		return temp

	temp.next=head
	head.pre=temp
	return temp

head1=_insert_beginning(head1,5)

def print_list(head):
	cur=head
	while cur!=None:
		print(cur.key)
		cur=cur.next

print_list(head1)