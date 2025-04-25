class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        ROWS = len(image)
        COLS = len(image[0])

        left = float("inf")
        right = float("-inf")
        top = float("inf")
        bottom = float("-inf")

        def dfs(r, c):
            nonlocal left, right, top, bottom
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or image[r][c] == "0":
                return
            image[r][c] = "0"

            left = min(left, c)
            right = max(right, c + 1)
            top = min(top, r)
            bottom = max(bottom, r + 1)

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(x, y)
        area = (right - left) * (bottom - top)
        return area
        