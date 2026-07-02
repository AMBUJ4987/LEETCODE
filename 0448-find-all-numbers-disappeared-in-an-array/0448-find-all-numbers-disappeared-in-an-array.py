class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        a=[]
        for i in range(1,n+1):
            if i not in set(nums):
                a.append(i)
        return a





        