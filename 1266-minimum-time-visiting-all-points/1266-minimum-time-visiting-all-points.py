class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        x1= points[0][0]
        y1 = points [0][1]
        points.pop(0)
        c = 0
        while points:
            x2 = points[0][0]
            y2=points[0][1]
            c += max(abs(x2-x1),abs(y2-y1))
            x1=x2
            y1=y2
            points.pop(0)
            
        return c


        

       