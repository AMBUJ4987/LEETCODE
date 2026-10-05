from typing import List

class Solution:

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        l = []

        while matrix:
            a = matrix.pop(0)
            l.extend(a)
            for i in matrix:
                if i:
                    l.append(i[-1])
                    i.pop()
            if matrix:
                b = matrix.pop(-1)
                l.extend(b[::-1])
            for i in range(len(matrix)-1,-1,-1):
                if matrix[i]:
                    l.append(matrix[i][0])
                    matrix[i].pop(0)
        return l
