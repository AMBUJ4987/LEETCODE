class Solution:
    def climbStairs(self, n: int) -> int:
        l = [0]*(n+1)
        c = len(l)-1
        if c==0:
            return 0
        if c==1:
            return 1
        if c ==2:
            return 2      
        l[0]=0
        l[1]=1
        l[2]=2
        for i in range(3,len(l)):
            l[i]=l[i-1]+l[i-2]
        return l[n]
        


        