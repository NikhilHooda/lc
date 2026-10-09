class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def union(edge1, edge2):
            parent1 = find(edge1)
            parent2 = find(edge2)
            parent[parent1] = parent2

        def find(edge):
            if parent[edge] != edge:
                parent[edge] = find(parent[edge])
            return parent[edge]

        parent = [i for i in range(n)]
        for edge1, edge2 in edges:
            union(edge1, edge2)
        hashSet = set()
        for edge in range(n):
            hashSet.add(find(edge))
        return len(hashSet)
