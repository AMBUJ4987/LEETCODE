from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l = []
        while matrix:
            l.extend(matrix.pop(0))

            for j in matrix:
                if j:
                    l.append(j.pop())

            if matrix:
                l.extend(matrix.pop()[::-1])

            for row in matrix[::-1]:
                if row: 
                    l.append(row.pop(0))

        return l

        