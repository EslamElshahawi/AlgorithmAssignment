class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))  # Initially, each vertex is its own parent
        self.rank = [0] * n  # Rank for union by rank

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(n, edges):
    # Step 1: Sort the edges by their weight
    edges.sort(key=lambda x: x[2])  # Sorting by edge weight
    
    # Step 2: Initialize disjoint-set data structure
    ds = DisjointSet(n)
    
    mst = []  # This will store the edges of the MST
    
    # Step 3: Iterate over the edges and apply union-find
    for u, v, weight in edges:
        if ds.find(u) != ds.find(v):
            mst.append((u, v, weight))
            ds.union(u, v)
    
    return mst

# Example usage:
n = 4  # Number of vertices
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]  # List of edges (u, v, weight)

mst = kruskal(n, edges)
print("Edges in the MST:", mst)
