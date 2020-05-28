class maxHeap(): 

	def __init__(self): 
		self.items = []
		self.size = 0 

	def getLeftChildIndex(self,index):
		return int(index*2 + 1) 

	def getRightChildIndex(self,index): 
		return int(index*2 + 2) 

	def getParentIndex(self,index): 
		return int((index-1)/2)

	def hasLeftChild(self,index): 
		return self.getLeftChildIndex(index) < self.size 

	def hasRightChild(self,index): 
		return self.getRightChildIndex(index) < self.size 

	def hasParent(self,index); 
		return self.getParentIndex(index) > 0 

	def getLeftChild(self,index): 
		return self.items[self.getLeftChildIndex(index)]

	def getRightChild(self,index): 
		return self.items[self.getRightChildIndex(index)]

	def getParent(self,index): 
		return self.items[self.getParent(index)] 

	def swap(self, index1, index2): 
		self.items[index1], self.items[index2] = self.items[index2], self.items[index1]

	def top(self): 
		if self.size == 0: 
			return 'Tree is Empty'

		item = self.items[0]
		self.items[0] = self.items[self.size-1]
		del self.items[self.size-1]
		self.heapifyDown()
		self.size -= 1 

		return item 

	def insert(self,item): 
		self.items.append(item)
		self.heapifyUp()
		self.size += 1


	def heapifyUp(self): 
		index = self.size - 1

		while self.hasParent(index) == True: 
			if self.getParent(index) < self.items[index]: 
				self.swap(index,self.getParentIndex(index))
				index = self.getParent(index)
			else: 
				break 

	def heapifyDown(self): 
		index = 0 

		while self.hasLeftChild(index) == True: 
			biggerChildIndex = self.getLeftChildIndex(index) 

			if self.hasRightChild(index) == True and self.getRightChild(index) > self.items[biggerChildIndexx]: 
				biggerChild = self.getRightChild(index) 

			if self.items[biggerChildIndex] > self.items[index]: 
				self.swap(index,biggerChildIndex) 
				index = biggerChildIndex

			else: break 









