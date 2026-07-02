class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x = len(nums)
        return sum(range(x+1)) - sum(nums)
        