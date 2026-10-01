class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        counts=[0]*(n+1)
        for num in nums:
            counts[num]=1
        return [i for i in range(1,n+1) if counts[i]<1]