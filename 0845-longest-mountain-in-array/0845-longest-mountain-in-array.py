class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr)<3:
            return 0
        c =0
        s=0
        d =[]
        for i in range(1,len(arr)-1):
            if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
                d.append(i)
        for i in d:
            l = i
            r = i
            while l>0 and arr[l]>arr[l-1]:
                l-=1
            while r< len(arr)-1 and arr[r]>arr[r+1]:
                r+=1
            for j in range(l,r+1):
                s+=1
            c = max(c,s)
            s = 0
        return c
        

