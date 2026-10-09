class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {"}":"{", "]":"[", ")":"("}
        if len(s) % 2 != 0:
            return False

        if not s:
            return False
    
        for p in s:
            if p in matches.values():
                stack.append(p)
            else:
                if stack:
                    if matches[p] == stack[-1]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if stack:
            return False
        else:
            return True
