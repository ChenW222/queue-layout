class Edge:
    def __init__(self, vertex1: int, vertex2: int):
        self.vertex1 = vertex1
        self.vertex2 = vertex2

    def __repr__(self):
        return f"Edge({self.vertex1}, {self.vertex1})"

    def __str__(self):
        return f"Edge {self.vertex1}-{self.vertex2}"