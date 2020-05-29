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

connections = [('A','B'),('C','B'),('B','D'),
	('E','F'),('F','C'),('A','C')]

graph = Graph(connections) 
print(graph._graph)



