class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        a = []
        for i in nums:
            a.append(i**2)
        b = sorted(a)
        return b
       
        