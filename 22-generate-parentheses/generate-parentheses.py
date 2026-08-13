class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #if openN < n, valid
        #if closedN < openN, valid
        stack = []
        res = []

        def backTrack(openN, closedN):
            #IIF
            if openN == closedN == n:
                ans = "".join(stack)
                res.append(ans)
                return
            
            if openN < n:
                stack.append("(")
                
                backTrack(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                
                backTrack(openN, closedN + 1)
                stack.pop()
              
        backTrack(0, 0)    
        return res
            
