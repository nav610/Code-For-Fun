class node():
	def __init__(self,value = None):
		self.value = value
		self.left_child = None
		self.right_child = None 
		self.parent = None

class binary_tree(): 
	def __init__(self):
		self.root = None 

	def insert(self,value):
		if self.root == None: 
			self.root = node(value) 
		else: self._insert(self.root,value)

	def _insert(self, cur_node, value):
		if cur_node.value > value: 
			if cur_node.left_child == None: 
				cur_node.left_child = node(value)
				cur_node.left_child.parent = cur_node
			else: self._insert(cur_node.left_child, value)
		
		elif cur_node.value < value: 
			if cur_node.right_child == None: 
				cur_node.right_child = node(value)
				cur_node.right_child.parent = cur_node
			else: self._insert(cur_node.right_child, value) 

		else: print("Value already in Tree!")

	def print_tree(self):
		if self.root != None: 
			self._print_tree(self.root)

	def _print_tree(self, cur_node):
		if cur_node != None: 
			self._print_tree(cur_node.left_child)
			print(str(cur_node.value)) 
			self._print_tree(cur_node.right_child)

	def height(self):
		if self.root != None:
			return self._height(self.root,0)
		else: return 0 

	def _height(self,cur_node,cur_height):
		if cur_node == None: return cur_height

		left_height = self._height(cur_node.left_child, cur_height+1)
		right_height = self._height(cur_node.right_child, cur_height+1) 
		return max(left_height, right_height)

	def search_tree(self,search):
		if self.root != None: 
			return self._search_tree(self.root,search)
		else: return(False)

	def _search_tree(self, cur_node, search): 
		if cur_node != None: 
			if search == cur_node.value:
				return(True)

			elif search < cur_node.value and cur_node.left_child != None: 
				return self._search_tree(cur_node.left_child, search) 
			elif search > cur_node.value and cur_node.right_child != None: 
				return self._search_tree(cur_node.right_child, search)
			return (False)
		
		elif cur_node == None: return(False)

	def find(self,x):
		if self.root != None: 
			if self.search_tree(x) == True: 
				return self._find(self.root,x)
			else: 
				print("Value is not in the Tree!")
				return None

	def _find(self,cur_node,x):
		if cur_node.value == x: 
			return cur_node
		if x > cur_node.value: 
			return self._find(cur_node.right_child,x)
		if x < cur_node.value: 
			return self._find(cur_node.left_child,x)
			
	def delete(self,x):
		if self.root != None and self.find(x) != None:
			del_node = self.find(x)
			return self._delete_node(del_node)

	def _delete_node(self,del_node): 
		
		#find min in tree
		def min_value_node(a_node):
			current = a_node
			while current.left_child != None: 
				current = current.left_child 
			return current 

		def num_children(a_node):
			num_children = 0 
			if del_node.left_child != None: num_children += 1
			if del_node.right_child != None: num_children += 1 
			return num_children 

		parent = del_node.parent 
		num_children = num_children(del_node)

		if num_children == 0: 
			if del_node == parent.left_child: 
				parent.left_child = None
			if del_node == parent.right_child: 
				parent.right_child = None 

		if num_children == 1: 
			if del_node.left_child != None: 
				child = del_node.left_child
			else: child = del_node.right_child 


			if parent.left_child == del_nod: 
				parent.left_child = child 
			else: parent.right_child = child 

			child.parent = parent

		if num_children ==2:

			successor = min_value_node(del_node.right_child)

			del_node.value = succesor.value()

			self._delete_node(succesor)


def fill_tree(tree, num_elems = 50, max_int = 1000): 
	from random import randint
	for _ in range(num_elems):
		elem = randint(0,max_int)
		tree.insert(elem)
	return tree 

tree = binary_tree()
tree = fill_tree(tree)
tree.insert(199)
print(tree.search_tree(199))

tree.delete(199)
print(tree.search_tree(199))
