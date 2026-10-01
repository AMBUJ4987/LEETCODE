class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        a = 0
        l=[]
      
        while a< len(nums):
            c=0
            for i in nums:
                if i<nums[a]:
                    c+=1
            l.append(c)
            a+=1
        return l
               
                      

             
        