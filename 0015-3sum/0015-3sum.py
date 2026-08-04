class Solution:
    def threeSum(self, nums):
        ans = []
        nums.sort()
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            while l<r:
                s = nums[l]+nums[r]
                if (s+nums[i])== 0:
                    ans.append((nums[i],nums[l],nums[r])) 
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r-=1                     
                elif (s+nums[i])<0:
                    l+=1
                else:
                    r-=1
        ans = set(ans)
                
        return list(ans)