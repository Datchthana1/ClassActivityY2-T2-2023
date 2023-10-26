class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = []

    def add_edge(self, vertex1, vertex2):
        self.vertices[vertex1].append(vertex2)

    def is_adjacent(self, vertex1, vertex2):
        return vertex2 in self.vertices[vertex1]

    def get_neighbors(self, vertex):
        return self.vertices[vertex]
    
    def get_all(self):
        print(self.vertices)

Name_Vertex = ""
g = Graph()
while True:
    length = int(input("โปรดระบุจำนวนจุดในกราฟแบบมีทิศทาง : "))
    if length > 2:
        break 
for i in range(length):
    vertex = str(input("โปรดระบุชื่อ Vertex : "))
    if vertex != "":
        vertex.upper()
        g.add_vertex(vertex)
    else:
        break
while True:
    print("โปรดระบุชื่อจุดที่เป็น Source และ Destinations ของเส้นเชื่อม")
    source = str(input("ชื่อจุดที่เป็น Source : "))
    destinations = str(input("ชื่อจุดที่เป็น Destinations : "))
    if source == "" and destinations == "" :
        break
    else:
        g.add_edge(source, destinations)
RootNode = str(input("โปรดระบุชื่อจุดที่เป็นจุดเริ่มต้นในการท่องไปในกราฟด้วยขั้นตอนวิธีแบบ Breacdth-First Search ชื่อจุดที่เป็นจุดเริ่มต้นในการท่องไปในกราฟ : "))