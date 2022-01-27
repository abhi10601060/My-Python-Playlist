class Node:
	def __init__(self,val):
		self.val=val
		self.next=None


class Queue:
	def __init__(self):
		self.head=None
		self.tail=None
		self.size=0


	def enque(self,x):

		temp=Node(x)
		
		self.size+=1

		if self.head==None:
			self.head=temp
			self.tail=temp
		else:
			self.tail.next=temp
			self.tail=temp
		return

	def deque(self):

		if self.head==None:
			return None
		temp=self.head.val

		if self.head==self.tail:
			self.head=None
			self.tail=None

		else:
			self.head=self.head.next

		self.size-=1

		return print(temp)

	def get_size(self):
		return	print(self.size)

	def get_first(self):
		return self.head.val

	def get_rear(self):
		return self.tail.val	

	def print(self):
		cur=self.head
		while cur!=None:
			print(cur.val,end=" ")
			cur=cur.next
		print( )
		return

s=Queue()

s.enque(5)
s.enque(10)
s.enque(6)
s.enque(9)
s.enque(8)
s.enque(1)

s.deque()

s.print()

s.deque()
s.enque(72)
s.deque()

s.print()

s.get_size()

print(s.get_first())
print(s.get_rear())