class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def can_place(d):
            count = 1
            last = position[0]

            for x in position[1:]:
                if x - last >= d:
                    count += 1
                    last = x

                    if count == m:
                        return True

            return False

        lo = 1
        hi = position[-1] - position[0]

        while lo <= hi:
            mid = (lo + hi) // 2

            if can_place(mid):
                lo = mid + 1
            else:
                hi = mid - 1

        return hi