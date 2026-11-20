class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        a=0
        l = []
        while a < len(nums):
            s=0
            for i in nums:
                if i < nums[a]:
                    s+=1
            l.append(s)
            a+=1
        return l
        

        
                      

             
        