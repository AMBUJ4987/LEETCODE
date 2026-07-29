class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a = {}
        
        n = target
        for i in range(len(numbers)):
            d = n - numbers[i]
            if d not in a:
                a[numbers[i]]=i
            else:
                return (a[d]+1,i+1)

            

                


        