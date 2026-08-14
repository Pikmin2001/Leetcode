class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def dfs(openN, closeN):
            #win con
            if openN == closeN == n:
                ans = "".join(stack.copy())
                res.append(ans)

            if openN < n:
                stack.append("(")
                dfs(openN+1, closeN)
                stack.pop()

            if closeN < openN:
                stack.append(")")
                dfs(openN, closeN+1)
                stack.pop()

        dfs(0, 0)
        return res 
        