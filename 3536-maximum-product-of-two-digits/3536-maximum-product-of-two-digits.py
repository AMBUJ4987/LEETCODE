class Solution:
    def maxProduct(self, n: int) -> int:
        mx1 = 0
        mx2 = 0

        while n:
            d = n % 10
            n //= 10

            if d >= mx1:
                mx2 = mx1
                mx1 = d
            elif d > mx2:
                mx2 = d

        return mx1 * mx2