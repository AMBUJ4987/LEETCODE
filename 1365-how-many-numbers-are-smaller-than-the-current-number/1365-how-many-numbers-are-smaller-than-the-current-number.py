class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l=[]
        for i in range(len(nums)):
            a=0
            for j in range(len(nums)):
                if nums[j]<nums[i]:
                    a+=1
            l.append(a) 
        return l      
                      

             
        