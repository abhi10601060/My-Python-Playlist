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

def insert_at_end(head,key):
	temp=Node(key)
	if head==None:
		temp.next==head
		return temp
	cur=head
	while cur.next!=None :
		cur=cur.next
	cur.next=temp
	temp.pre=cur
	return head

head=insert_at_end(head,40)

def print_list(head):
	cur=head
	while cur!=None:
		print(cur.key)
		cur=cur.next

# print_list(head)

head1=None

head1=insert_at_end(head1,45)
head1=insert_at_end(head1,55)

print_list(head1)