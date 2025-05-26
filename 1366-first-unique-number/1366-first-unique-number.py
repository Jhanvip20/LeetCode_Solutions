class FirstUnique:

    def __init__(self, nums: List[int]):
        self.q = deque(nums)
        self.count = Counter(nums)

    def showFirstUnique(self) -> int:
        while self.q and self.count[self.q[0]] > 1:
            self.q.popleft()

        if not self.q:
            return -1

        return self.q[0] 

    def add(self, value: int) -> None:
        self.q.append(value)
        self.count[value] += 1
    
# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)