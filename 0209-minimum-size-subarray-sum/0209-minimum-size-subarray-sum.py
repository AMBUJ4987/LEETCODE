class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l = []
        c = float("inf")
        s = 0
        for i in range(len(nums)):
            l.append(nums[i])
            s+=nums[i]
            while s>= target:
                c = min(c,len(l))
                s-= l.pop(0)
        if c == float("inf"):
            return 0
        return c
        