class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = 1
        postfix = 1
        res = [1]*len(nums)

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        print(f"prefix: {res}")
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res       