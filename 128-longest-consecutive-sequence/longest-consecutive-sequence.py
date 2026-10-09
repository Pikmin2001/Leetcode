class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        seen = set(nums)
        maxSeq = 0
        for n in seen:
            if n-1 not in seen:
                seq = 1
                while n+1 in seen:
                    n+=1
                    seq += 1
                maxSeq = max(maxSeq, seq)

        return maxSeq