from collections import defaultdict

class Graph(): 
	def __init__(self, connections):
		self._graph = defaultdict(set)
		self.add_connections(connections)

	def add_connections(self,connections):
		for node1, node2 in connections:
			self._add(node1,node2)

	def _add(self, node1, node2): 
		self._graph[node1].add(node2)

	def remove(self, node): 
		try: 
			for key, values in self._graph: 
				values.remove(node)
		except KeyError: pass

		try: 
			del self._graph[node]
		except KeyError: pass

	def hasPathDFS(self, source, destination):
		visited = set()
		return self._hasPathDFS(source, destination, visited) 


	def _hasPathDFS(self, source, destination, visited): 
		if source == destination: 
			return True 

		if source in visited: 
			return False

		visited.add(source)

		for node in self._graph[source]: 
			return self._hasPathDFS(node, destination, visited)


		return False 

	def hasPathBFS(self, source, destination): 
		listToLook = [] 
		visited = set()
		listToLook.append(source)

		while len(listToLook) != 0: 
			node = listToLook[0]
			del listToLook[0]

			if node == destination: 
				return True

			if node in visited: 
				continue 

			visited.add(node) 

			for child in self._graph[node]:
				listToLook.append(child) 

		return False 



#connections = [('A','B'),('C','B'),('B','D'),
	('E','F'),('F','C'),('A','C')]

#graph = Graph(connections) 
#print(graph._graph)
#print(graph.hasPathDFS('A','D'))


