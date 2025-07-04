class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        A=0
        for b in range((k-1).bit_length()):
            A|=(operations[b]<<b)
        return chr(97+((k-1) & A).bit_count()%26)

               