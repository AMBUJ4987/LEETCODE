class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i,n in enumerate(nums):
            s = target- n
            
            if s in a:
                return [i,a[s]]
            a[n]=i
            
            