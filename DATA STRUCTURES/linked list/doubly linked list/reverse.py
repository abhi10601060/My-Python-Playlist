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


def revesre(head):
	if head==None or head.next==None:
		return head
	cur=head
	pre=None
	while cur.next!=None:
		next_node=cur.next 
		cur.next=pre
		cur.pre=next_node
		pre=cur
		cur=next_node
	cur.pre=None
	cur.next=pre
	return cur

head=revesre(head)

def print_list(head):
	cur=head
	while cur!=None:
		print(cur.key)
		cur=cur.next

print_list(head)

# head1=None
# head1=revesre(head1)
# print_list(head1)
