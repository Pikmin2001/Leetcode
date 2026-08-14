class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows = len(board)
        cols = len(board[0])
        path = set()
        # i = current letter of word we are searching for
        def dfs(r, c, i):
            #win con
            if i == len(word):
                return True
            
            if r < 0 or c < 0  or r >= rows or c >= cols or board[r][c] !=  word[i] or (r, c) in path:
                return False
                #check surrounding for word[i+1]
            path.add((r, c))
            res = (dfs(r+1, c, i+1) or  
            dfs(r, c+1, i+1) or
            dfs(r-1, c, i+1) or
            dfs(r, c-1, i+1))
            path.remove((r,c))
            return res

        for j in range(rows):
            for k in range(cols):
                if dfs(j, k, 0) == True:
                    return True
        return False
        