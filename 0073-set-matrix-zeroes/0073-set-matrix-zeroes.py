class Solution:
    def setZeroes(self, g: List[List[int]]) -> None:
        m,n=len(g),len(g[0])
        r,c=map(set,zip(*((i,j) for i,j in product(range(m),range(n)) if g[i][j]==0),(-1,-1)))
        for i,j in product(range(m),range(n)):
            if i in r or j in c: g[i][j]=0
        