class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a = len(nums)
        b = 0
        for i in range(a+1):
            if i in nums:
                continue
            b = i
        return b

       


       