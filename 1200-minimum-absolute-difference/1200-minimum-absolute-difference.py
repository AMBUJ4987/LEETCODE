class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        l = []
        arr.sort()
        k = float('inf')
        for i in range(len(arr)-1):
            d = abs(arr[i]-arr[i+1])
            if d < k:
                l.clear()
                l.append([arr[i],arr[i+1]])
                k = d
            elif d==k and [arr[i],arr[i+1]] not in l:
                l.append([arr[i],arr[i+1]])


        return l
                       



        