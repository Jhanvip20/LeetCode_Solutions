class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def f(v):
            yield from (q for u in range(v,v+10-(v==1)) if u<=n for q in [u,*f(u*10)])
        return [*f(1)]
        