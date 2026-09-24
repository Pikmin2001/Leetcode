class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        pac = set()
        atl = set()
        res = []

        ROWS, COLS = len(heights), len(heights[0])

        def dfs(r, c, ocean, prevHeight):
            if ((r, c) in ocean or r not in range(ROWS) or c not in range(COLS)) or heights[r][c] < prevHeight:
                return

            ocean.add((r, c))
            dfs(r + 1, c, ocean, heights[r][c])
            dfs(r - 1, c, ocean, heights[r][c])
            dfs(r, c + 1, ocean, heights[r][c])
            dfs(r, c - 1, ocean, heights[r][c])
            
        #loop   1
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])

        # loop  2
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, atl, heights[r][COLS-1])
        
        #master loop
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res