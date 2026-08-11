class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {}
        tDict = {}
        for char in s:
            sDict[char] = 1 + sDict.get(char, 0)
        
        for char in t:
            tDict[char] = 1+ tDict.get(char, 0)

        if sDict == tDict:
            return True
        return False
        