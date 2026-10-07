class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sDict, tDict = {}, {}
        for n in s:
            sDict[n] = 1 + sDict.get(n, 0)
        for n in t:
            tDict[n] = 1 + tDict.get(n, 0)

        if tDict == sDict:
            return True
        return False