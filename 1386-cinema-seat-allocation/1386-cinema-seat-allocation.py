from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = defaultdict(set)

        for r, s in reservedSeats:
            rows[r].add(s)

        ans = 2 * n

        for seats in rows.values():

            left = all(s not in seats for s in [2, 3, 4, 5])
            middle = all(s not in seats for s in [4, 5, 6, 7])
            right = all(s not in seats for s in [6, 7, 8, 9])

            if left and right:
                # We can put two groups
                continue

            elif left or middle or right:
                # Only one group can fit
                ans -= 1

            else:
                # No group can fit
                ans -= 2

        return ans