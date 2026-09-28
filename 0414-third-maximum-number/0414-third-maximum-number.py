class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        nums=list(set(nums))
        nums.sort()
        nums.reverse()
        if len(nums)<3:
            return nums[0]
        return nums[2]

        