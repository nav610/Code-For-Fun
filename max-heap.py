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

	def hasParent(self,index): 
		return self.getParentIndex(index) >= 0 

	def getLeftChild(self,index): 
		return self.items[self.getLeftChildIndex(index)]

	def getRightChild(self,index): 
		return self.items[self.getRightChildIndex(index)]

	def getParent(self,index): 
		return self.items[self.getParentIndex(index)] 

	def swap(self, index1, index2): 
		self.items[index1], self.items[index2] = self.items[index2], self.items[index1]

	def top(self): 
		if self.size == 0: 
			return 'Tree is Empty'
		else: 
			return self.items[0] 

	def takeTop(self):
		if self.size == 0: 
			return 'Tree is Empty'

		item = self.items[0]
		self.items[0] = self.items[self.size-1]
		del self.items[self.size-1]
		self.size -= 1
		self.heapifyDown()
		return item 

	def insert(self,item): 
		self.items.append(item)
		self.heapifyUp()
		self.size += 1


	def heapifyUp(self): 
		index = self.size

		while self.hasParent(index) == True: 
			if self.getParent(index) < self.items[index]: 
				self.swap(index,self.getParentIndex(index))
				index = self.getParentIndex(index)
			else: 
				break 

	def heapifyDown(self): 
		index = 0

		while self.hasLeftChild(index) == True: 
			biggerChildIndex = self.getLeftChildIndex(index) 

			if self.hasRightChild(index) == True and self.getRightChild(index) > self.items[biggerChildIndex]: 
				biggerChild = self.getRightChild(index) 

			if self.items[biggerChildIndex] > self.items[index]: 
				self.swap(index,biggerChildIndex) 
				index = biggerChildIndex

			else: break 

maxHeap = maxHeap()

for i in [0,1,2,45,82,12,43,92,111,305,31,10]: 
	maxHeap.insert(i)
print(maxHeap.items)

maxHeap.takeTop()
print(maxHeap.items)







