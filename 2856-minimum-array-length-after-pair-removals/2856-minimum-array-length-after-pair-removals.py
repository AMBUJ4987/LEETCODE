class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)

        maxFreq = 1
        cnt = 1

        for i in range(1, n):
            if nums[i] == nums[i-1]:
                cnt += 1
            else:
                maxFreq = max(maxFreq, cnt)
                cnt = 1

        maxFreq = max(maxFreq, cnt)

        if maxFreq > n // 2:
            return 2 * maxFreq - n
        return n % 2