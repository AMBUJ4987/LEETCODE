class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        a = len(nums)
        l = [0]*(a+1)
        s = []
        for i in nums:
            l[i]=1
        for i in range(1,a+1):
            if l[i]<1:
                s.append(i)
        return s