class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        s =set()
        for i,val in enumerate(nums):
            if val in s:
                return True
            s.add(val)
            if len(s)>k:
                s.remove(nums[i-k])
        
        return False

        