class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        l = []
        a = min(nums)
        b = max(nums)        
        for j in range(a,b+1):
            if j not in nums:
                l.append(j)
        return l





        