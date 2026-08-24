class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        smallS = min(strs)

        for i in range(len(smallS)):
            for s in strs:
                if smallS[i] == s[i]:
                    continue
                else:
                    return prefix
            prefix += smallS[i]
        return prefix
        