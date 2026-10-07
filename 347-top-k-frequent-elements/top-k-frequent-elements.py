class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        res = []
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        sortedN = sorted(count, key=count.get)
        for i in range(k):
            res.append(sortedN.pop())
        return res