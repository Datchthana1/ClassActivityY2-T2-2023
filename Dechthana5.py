class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = []

    def add_edge(self, vertex1, vertex2):
        self.vertices[vertex1].append(vertex2)
        self.vertices[vertex2].append(vertex1)

    def is_adjacent(self, vertex1, vertex2):
        return vertex2 in self.vertices[vertex1]

    def get_neighbors(self, vertex):
        return self.vertices[vertex]
    
    def get_all(self):
        print(self.vertices)
    
graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")
graph.add_edge("A","B")
graph.add_edge("A","C")
graph.add_edge("B","D")
graph.add_edge("C","D")
graph.add_edge("C","E")
print(graph.is_adjacent("A", "B"))
print(graph.get_all())