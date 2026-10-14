class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        l = set()
        for i,v in enumerate(nums):
            if v in l:
                return True
            l.add(v)
            if len(l)>k:
                l.remove(nums[i-k])
        return False             
                
                

        