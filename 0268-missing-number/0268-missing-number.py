class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x = len(nums)
        t = (x**2 + x ) //2
        for i in nums:
            t = t-i
        return t    
        