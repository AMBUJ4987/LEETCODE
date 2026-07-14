from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        c = [0, 0]

        for s in students:
            c[s] += 1

        for s in sandwiches:
            if c[s] == 0:
                break
            c[s] -= 1

        return c[0] + c[1]