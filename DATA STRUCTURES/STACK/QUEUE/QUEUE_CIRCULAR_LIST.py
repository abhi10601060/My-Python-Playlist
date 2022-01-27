class Queue:
	def __init__(self,c):
		self.list=[None]*c
		self.cap=c 
		self.size=0
		self.front=0
		self.rear=(self.front+self.size-1)%c


	def enque(self,x):

		if self.list[(self.rear+1)%self.cap]!=None and self.rear==self.front:
			return print("Queue is Full...!!")
	
		self.rear=(self.rear+1) % self.cap

		self.list[self.rear]=x
		self.size+=1

		return 


	def deque(self):

		if self.front==None:
			return print("Queue is empty..!!!")

		self.list[self.front]=None

		self.front=(self.front+1)%self.cap

		self.size-=1

		return

	def print(self):

		print(self.list)

		return 


	def get_front(self):
		return print(self.front)

	def get_rear(self):
		return print(self.rear)




q=Queue(3)
q.enque(50)
q.enque(40)
q.enque(70)
q.enque(90)
q.deque()
q.enque(80)
# q.deque()
q.enque(50)
q.print()

