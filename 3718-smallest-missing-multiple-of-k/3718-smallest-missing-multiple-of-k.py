class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums.sort()
        a = max(nums)
        for i in range(0,a+k+1,k):
            if i != 0 and i %k ==0 and i not in nums:
                return i


      