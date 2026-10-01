class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a = len(nums)
        s = (a*(a+1))//2
        for i in nums:
            s -=i
        return s
        


       