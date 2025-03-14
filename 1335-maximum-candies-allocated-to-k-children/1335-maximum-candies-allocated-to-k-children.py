class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def isValidSize(group_candies):
            groups = 0
            for candy in candies:
                groups += candy // group_candies # add groups that can be made from candy
            return groups >= k

        left, right = 0, sum(candies) // k # min is 0 candy per group, max is split all candies evenly

        while left < right: # binary search to find max number of candies per group
            mid = 1 + (left + right) // 2 # 1 + or ceil( / 2) to avoid looping with left = mid
            
            if isValidSize(mid): # true if can make k groups of mid size
                left = mid # valid group, move left up and check higher group sizes
            else:
                right = mid - 1 # invalid group, move right down and check lower group sizes
        
        return left # left = right = max valid size. right + 1 is first invalid size
        