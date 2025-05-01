class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.food = food
        self.path = [[0,0]]
        self.eat = 0
        
    def move(self, direction: str) -> int:
        x, y = self.path[0]
        if direction == 'U':
            x = x - 1
        elif direction == 'L':
            y = y - 1
        elif direction == 'R':
            y = y + 1
        elif direction == 'D':
            x = x + 1
        if [x,y] in self.path[:-1] or x<0 or x>=self.height or y < 0 or y >=self.width:
            return -1
        self.path.insert(0, [x,y])
        
        if self.eat < len(self.food) and [x,y] == self.food[self.eat]:
            self.eat+=1
        else:
            self.path.pop()
            
        return self.eat


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)