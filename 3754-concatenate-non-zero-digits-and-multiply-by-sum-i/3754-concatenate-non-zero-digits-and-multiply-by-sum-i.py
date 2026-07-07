class Solution:
    def sumAndMultiply(self, n: int) -> int:
        a = ""
        b = 0
        for ch in str(n):
            digit = int(ch)
            if digit == 0:
                continue
            a += ch
            b += digit

        if a == "":
            return 0

        return int(a) * b