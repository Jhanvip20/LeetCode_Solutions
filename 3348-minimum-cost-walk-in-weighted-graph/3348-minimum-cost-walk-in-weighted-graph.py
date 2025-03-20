class UnionFind:
    def __init__(self):
        self.parents = {}
    
    def union(self, el1, el2):
        self.parents[self.find(el2)] = self.find(el1)

    def find(self, el):
        parent = self.parents.setdefault(el, el)
        if el != parent: parent = self.parents[el] = self.find(parent)
        return parent
    
    def __contains__(self, el):
        return self.find(el) != el
class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        g, uf = defaultdict(list), UnionFind()
        for v,u,w in edges:
            g[v].append((u,w))
            g[u].append((v,w))
        
        def dfs(v,u):
            if u in uf: return -1
            uf.union(v,u)
            return reduce(lambda q,p:q&dfs(v,p[0])&p[1],g[u],-1)

        node2MinW = {v:dfs(v,v) for v in range(n)}

        return [[-1,node2MinW[uf.find(s)]][uf.find(s)==uf.find(t)] for s,t in query]
    
    