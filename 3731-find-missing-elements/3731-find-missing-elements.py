class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        l = []
        nums.sort()        
        for j in range(nums[0],nums[-1]+1):
            if j not in nums:
                l.append(j)
        return l





        