class minHeap():
	def __init__(self):
		self.size = 0 
		self.items = []
		
	def getLeftChildIndex(self, parentIndex):
		return int(parentIndex*2 + 1)

	def getRightChildIndex(self, parentIndex):
		return int(parentIndex*2 + 2 )

	def getParentIndex(self, childIndex):
		return int((childIndex-1)/2)

	def hasLeftChild(self, index): 
	 	return getLeftChildIndex(index) < size

	def hasRightChild(self, index):
	 	return getRightChildIndex(index) < size

	def hasParent(self, index): 
	 	return self.getParentIndex(index) >= 0 

	def getLeftChild(self, index): 
	 	return self.items[self.getLeftChildIndex(index)]

	def getRightChild(self, index): 
	 	return self.items[self.getRightChildIndex(index)]

	def getParent(self, index): 
	 	return self.items[self.getParentIndex(index)]

	def swap(self, index1, index2):
	 	self.items[index1], self.items[index2] = self.items[index2], self.items[index1]

	def top(self): 
	 	if self.size == 0: 
	 		return 'Nothing in Tree'

	 	else:
	 		return self.items[0]

	def takeTop(self): 
	 	if self.size == 0: return 'Nothing in Tree'
	 	
	 	top = self.items[0]
	 	self.items[0] = self.items[size-1]
	 	del self.items[self.size-1]
	 	self.size -= 1
	 	self.heapifyDown()
	 	return top


	def insert(self,item):
		self.items.append(item)
		self.heapifyUp()
		self.size += 1

	def heapifyUp(self): 
		index = self.size - 1

		while self.hasParent(index) == True: 
			if self.items[index] < self.items[self.getParentIndex(index)]: 
				self.swap(index,self.getParentIndex(index)) 
				index = self.getParentIndex(index)

			else: 
				break

	def heapifyDown(self): 
		index = 0 

		while self.hasLeftChild(index) == True:
			smallerChildIndex = self.getLeftChildIndex(index)

			if self.hasRightChild(index) == True and items[smallerChildIndex] > items[self.getRightChildIndex(index)]: 
				smallerChildIndex = self.getRightChildIndex(index)

			if items[index] > items[smallerChildIndex]: 
				break

			else:
				swap(index,smallerChildIndex)
			index = smallerChildIndex










