class Solution:
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:
        turn_on = [0 for _ in range(len(bulbs))]
        
        for day, pos in enumerate(bulbs):
            turn_on[pos-1] = day
        
        ans = -1
        
        left = 0
        right = left + k + 1
        for pos, day in enumerate(turn_on):
            if right >= len(turn_on):
                break
            maxDay = max(turn_on[left], turn_on[right])
            
            if day > maxDay:
                continue
            
            if pos == right:
                if maxDay < ans or ans == -1:
                    ans = maxDay + 1
            left = pos
            right = left + k + 1
        return ans