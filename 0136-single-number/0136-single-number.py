class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        c = 0
        for i in nums:
            c^=i
        return c
        