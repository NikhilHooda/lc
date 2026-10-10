class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        parent1 = self.find(node1)
        parent2 = self.find(node2)
        
        if parent1 == parent2:
            return False
        
        if self.rank[parent1] >= self.rank[parent2]:
            self.parent[parent2] = parent1
            self.rank[parent1] += self.rank[parent2]
        else:
            self.parent[parent1] = parent2
            self.rank[parent2] += self.rank[parent1]
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailToAcc = {} #email -> idx of acc

        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailToAcc:
                    uf.union(emailToAcc[e], i)
                else:
                    emailToAcc[e] = i
        
        emailGroup = defaultdict(list) # idx : [emails]
        for email, i in emailToAcc.items():
            leader = uf.find(i)
            emailGroup[leader].append(email)
        
        res = []
        for i, emails in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(emails))
        return res
