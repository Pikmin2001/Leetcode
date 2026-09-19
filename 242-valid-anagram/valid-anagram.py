class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {}
        tDict = {}
        
        for l in s:
            sDict[l] = 1 + sDict.get(l, 0)

        for l in t:
            tDict[l] = 1 + tDict.get(l, 0)

        if sDict == tDict:
            return True
        else:
            return False