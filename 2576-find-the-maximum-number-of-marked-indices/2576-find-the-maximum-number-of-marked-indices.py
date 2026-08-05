class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()

        n = len(nums)
        i = 0
        j = (n + 1) // 2
        ans = 0

        while i < (n + 1) // 2 and j < n:
            if 2 * nums[i] <= nums[j]:
                ans += 2
                i += 1
                j += 1
            else:
                j += 1

        return ans