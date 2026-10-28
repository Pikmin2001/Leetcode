class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
            ROWS, COLS = len(grid), len(grid[0])
            islands = 0
            seen = set()

            def bfs(r, c):
                queue = collections.deque()
                queue.append((r, c))
                while queue:
                    r, c = queue.popleft()
                    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                    for dr, dc in directions:
                        if r+dr in range(ROWS) and c+dc in range(COLS) and grid[r+dr][c+dc] == '1' and (r+dr, c+dc) not in seen:
                            seen.add((r+dr, c+dc))
                            queue.append((r+dr, c+dc))
                
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c]=='1' and (r, c) not in seen:
                        bfs(r, c)
                        islands += 1
            return islands

