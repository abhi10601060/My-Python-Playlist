from collections import deque


class Queue:
	
	def __init__(self ):

		self.q=deque()
		self.max=deque()

	def enque(self, x):
		self.q.append(x)

		while self.max and self.max[-1]<x:
			self.max.pop()

		self.max.append(x)

	def deque(self):
		if self.q:
			result=self.q.popleft()

			if result==self.max[0]:
				self.max.popleft()

			return result
		else:
			print("Queue is Empty...")

	def get_max(self):
		if self.max:
			return print(self.max[0])
		return print("Queue is Empty...")

	def print(self):
		return print(self.q)


q=Queue()
q.enque(50)
# q.deque()
q.enque(80)
q.enque(78)
q.enque(96)
q.enque(12)
q.deque()
q.print()
q.get_max()