class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        seen = set()

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            while q:
                dr, dc = q.popleft()
                directions = [(dr+1, dc), (dr, dc+1), (dr-1, dc), (dr, dc-1)]
                for dr, dc in directions:
                    if dr in range(ROWS) and dc in range(COLS) and grid[dr][dc] == '1' and (dr, dc) not in seen:
                        seen.add((dr, dc))
                        q.append((dr, dc))



        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in seen:
                    seen.add((r, c))
                    bfs(r, c)
                    islands += 1
        return islands

        