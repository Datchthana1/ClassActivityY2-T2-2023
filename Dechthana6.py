class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [ ]

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find_set(self, parent, i):
        if i != parent[i]:
            parent[i] = self.find_set(parent, parent[i])
        return parent[i]
   
    def union(self, parent, rank, x, y):
        x = self.find_set(parent, x)
        y = self.find_set(parent, y)
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] = rank[x] + 1   

    def kruskal(self):
        A = [ ]
        self.graph = sorted(self.graph, key = lambda item: item[2])       
        parent = [ ]
        rank = [ ]
        for vertex in range(self.V):
            parent.append(vertex)
            rank.append(0)       
        i = 0
        e = 0
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find_set(parent, u)
            y = self.find_set(parent, v)
            if x != y:
                e = e + 1
                A.append([u, v, w])
                self.union(parent, rank, x, y)
                print(f"เส้นเชื่อมระหว่างจุด {u} กับจุด {v} น้ำหนัก = {w}")       
        sum = 0
        for u, v, weight in A:
            sum = sum + weight
        print(f"ค่าน้ำหนักรวมของ Mininum Spanning Tree : {sum}")

while True:
    ValuePoint = int(input("โปรดระบุจำนวนจุดในกราฟแบบไม่มีทิศทาง(Undirection graph) ที่มีค่ามากกว่า 2 : "))
    if ValuePoint > 2:
        G = Graph(ValuePoint)
        break
EdgePoint = int(input("โปรดระบุเส้นเชื่อม (Edge) : "))
print("โปรดระบชื่อที่เป็น Source ชื่อจุดที่เป็น Destination ค่าน้ำหนัก Weight ของเส้นเชื่อม ")
while True:
    Source = int(input("Source : "))
    Destination = int(input("Destination : "))
    Weight = int(input("น้ำหนัก : "))
    G.addEdge(Source,Destination,Weight)
    EdgePoint -= 1
    if EdgePoint == 0:
        print("Minimum Spaning Tree คือ ")
        G.kruskal()
        break
