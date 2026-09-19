class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = { ")" : "(", "]" : "[", "}" : "{" }
        stack = []
        openn = ["[", "(", "{"]
        close = ["]", ")", "}"]
        if len(s) % 2 != 0:
            return False
        
        for p in s:
            if p in openn:
                stack.append(p)
            else:
                if p in dictionary.keys():
                    if stack and dictionary[p] == stack.pop():
                        continue
                    else:
                        return False 
        if len(stack) != 0:
            return False
        return True