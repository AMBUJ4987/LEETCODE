class Solution:
    def maxDepth(self, s: str) -> int:
        a = 0
        st = 0
        s= str(s)
        for i in s:
            if i == '(':
                a+=1
            if i == ')':
                a-=1
            st = max(st,a)
        return st