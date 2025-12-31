class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def canCross(day: int) -> bool:
            grid = [[0] * col for _ in range(row)]
            for i in range(day):
                r, c = cells[i]
                grid[r - 1][c - 1] = 1

            q = deque()
            for c in range(col):
                if grid[0][c] == 0:
                    q.append((0, c))
                    grid[0][c] = 1

            while q:
                x, y = q.popleft()
                if x == row - 1:
                    return True
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < row and 0 <= ny < col and grid[nx][ny] == 0:
                        grid[nx][ny] = 1
                        q.append((nx, ny))
            return False

        left, right = 0, row * col
        while right - left > 1:
            mid = (left + right) // 2
            if canCross(mid):
                left = mid
            else:
                right = mid
        return left