class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        maxKey = len(mat) + len(mat[0]) - 2
        B = [[] for _ in range(maxKey + 1)]

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                tmp = B[i + j]
                tmp.append([mat[i][j], len(mat[0]) * i + j])

        res = []

        for k in range(maxKey + 1):
            v = B[k]
            res.append(sorted(v, key=lambda x: x[1]) if k & 1 else sorted(v, key=lambda x: -x[1]))

        return [c[0] for sublist in res for c in sublist]