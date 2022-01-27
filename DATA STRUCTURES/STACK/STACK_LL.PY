class Node:
	def __init__(self,val):
		self.val=val
		self.next=None

class stack:

	def __init__(self):
		self.head=None
		self.z=0

	def push(self,n):
		temp=Node(n)
		temp.next=self.head
		self.head=temp
		self.z+=1

	def size(self):
		return self.z 

	def pop(self):
		if self.head==None:
			return "error"

		res=self.head.val
		self.head=self.head.next
		self.z-=1
		return res

	def peek(self):
		return self.head

s=stack()

s.push(3)
print(s.pop())
print(s.pop())
s.pop()
s.push(54)
s.push(5)
print(s.size())


