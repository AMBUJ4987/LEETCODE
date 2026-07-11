class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l=[]
        d={}
        temp = sorted(nums)
        for i,num in enumerate(temp):
            if num not in d:
                d[num]=i
        for n in nums:
            l.append(d[n])   
        return l         
            

               
                      

             
        