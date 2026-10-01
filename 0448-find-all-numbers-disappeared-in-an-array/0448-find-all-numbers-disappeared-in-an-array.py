class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)

        nums = set(nums)
        b=[]
        a = [0] * (n+1)
        for i in nums:
            a[i]=1
        for i in range(len(a)):
            if i == 0:
                continue
            if a[i] == 1:
                continue
            b.append(i)
        return b
            
            
        



        