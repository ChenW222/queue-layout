from typing import List
from Edge import Edge
class Vertices:
    def __init__(self):
        self.vertices = {}

    def create_vertices(self, size_s: str):
        size = int(size_s)
        for i in range(1, size + 1):
            self.vertices[i] = []

    def add_edge(self, edge: str):
        parts = edge.strip().split()
        i1 = int(parts[1])
        i2 = int(parts[2])

        #assumes there are no loops
        self.vertices[i1].append(i2)
        self.vertices[i2].append(i1)

    def find_queue_index(self, entry, vt):
        left = 1
        right = len(entry) - 1

        while left <= right:
            mid = (left + right) // 2
            if entry[mid] <= vt < entry[mid - 1]:
                return mid - 1
            elif vt >= entry[mid - 1]:
                right = mid - 1
            else:
                left = mid + 1
        return None  # Not found

    def get_queue(self) -> List[List[Edge]]:
        queue = [[] for _ in range(len(self.vertices) // 2)]

        # create entry array
        entry = [0] * (len(self.vertices) + 2)
        entry[0] = len(self.vertices) + 1

        # vs = current vertex
        for vs, neighbors in self.vertices.items():
            for vt in neighbors:
               if vs < vt:           
                    idx = self.find_queue_index(entry, vt)
                    if idx is not None:
                        queue[idx].append(Edge(vs, vt))


            # adjust the entry array
            for vt in neighbors:
                if vs < vt:
                    entry = self.adjust_entry(entry, vt)

        return queue
    
    def adjust_entry(self, entry: List[int], t: int) -> List[int]:
        for i in range(1, len(entry)):
            if entry[i] == t:
                break
            elif t > entry[i]:
                entry[i] = t
                break
        return entry


    def __str__(self):
        return_string = ""
        for key, value in self.vertices.items():
            return_string += f"Vertex {key}:\n"
            for v in value:
                return_string += f"{key}-{v}\n"
        return return_string

