class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int: 
        n = len(colors)
        count = 0
        left = 0

        for right in range(n + k - 1):
            if right > 0 and colors[right % n] == colors[(right - 1) % n]:
                left = right  
            
            if right - left + 1 >= k:
                count += 1  
        
        return count