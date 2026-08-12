class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)

        for start, end, direction in shifts:
            if direction == 1:
                diff[start] += 1
                diff[end + 1] -= 1
            else:
                diff[start] -= 1
                diff[end + 1] += 1

        ans = []
        curr = 0

        for i in range(n):
            curr += diff[i]

            x = ord(s[i]) - ord('a')
            x = (x + curr) % 26
            ans.append(chr(x + ord('a')))

        return "".join(ans)