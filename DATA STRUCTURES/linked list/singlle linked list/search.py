class node:
	def __init__(self,key):
		self.key=key
		self.next=None

head=node(10)
head.next=node(20)
head.next.next=node(30)
head.next.next.next=node(40)


def search(head,key):
	cur=head
	idx=1
	while cur!=None:
		if cur.key==key:
			return idx
		cur=cur.next
		idx+=1
	return -1
print(search(head,40))
