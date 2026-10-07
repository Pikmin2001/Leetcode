class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        words = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            words[key].append(s)

        return list(words.values())
