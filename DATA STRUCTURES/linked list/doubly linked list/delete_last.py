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

def del_last(head):
	if head==None or head.next==None:
		return None

	cur=head
	while cur.next.next!=None:
		cur=cur.next
	cur.next=None
	return head

head=del_last(head)

def print_list(head):
	cur=head
	while cur!=None:
		print(cur.key)
		cur=cur.next

print_list(head)
