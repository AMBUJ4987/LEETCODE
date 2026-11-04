class Solution:
    def maxDistance(self, moves: str) -> int:
        x1=0
        y1=0
        c=0
        for i in moves:
            if i== 'U':
                x1+=1
            elif i == 'D':
                x1-=1
            elif i == 'L':
                y1-=1
            elif i == 'R':
                y1+=1
            else:
                c+=1
        a = abs(x1)+abs(y1)+c
        return a



        