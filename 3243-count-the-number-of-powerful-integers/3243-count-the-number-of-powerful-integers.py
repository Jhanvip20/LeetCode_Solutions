class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        cnt_start = str(start - 1)
        cnt_finish = str(finish)
        return self.cnt(cnt_finish, s, limit) - self.cnt(cnt_start, s, limit)

    def cnt(self, num: str, suffix: str, limit: int) -> int:
        if len(num) < len(suffix):
            return 0
        if len(num) == len(suffix):
            return 1 if num >= suffix else 0
        
        res = 0
        prefix = len(num) - len(suffix)
        
        for i in range(prefix):
            digit = int(num[i])
            if digit > limit:
                res += (limit + 1) ** (prefix - i)
                return res
            res += digit * (limit + 1) ** (prefix - i - 1)
        
        if num[-len(suffix):] >= suffix:
            res += 1
        
        return res

