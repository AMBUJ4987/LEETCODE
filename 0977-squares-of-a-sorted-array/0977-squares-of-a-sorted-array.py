from collections import deque 
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        a = deque()
        l,r = 0, len(nums)-1
        while l<=r:
            left,right = abs(nums[l]),abs(nums[r])
            if left > right:
                a.appendleft(left*left)
                l +=1
            else:
                a.appendleft(right*right)
                r-=1

        return list(a)

       