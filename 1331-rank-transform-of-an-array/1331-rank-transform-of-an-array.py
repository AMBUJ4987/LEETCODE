class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        l = []
        d = {}
        temp = sorted(set(arr))
        for i, num in enumerate(temp,start=1):
            if num not in d:
                d[num]= i
        for i in arr:
            l.append(d[i])
        return l    







