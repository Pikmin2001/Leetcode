class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        dictionary = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        res = []
        combos = []

        def dfs(i):
            if i == len(digits):
                res.append("".join(combos))
                return 
            
            for letter in dictionary[digits[i]]:
                combos.append(letter)
                dfs(i+1)
                combos.pop()

        dfs(0)
        return res