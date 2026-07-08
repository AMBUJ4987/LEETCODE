from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        # prefix count of non-zero digits
        cnt = [0] * (n + 1)

        # prefix sum of non-zero digits
        digit_sum = [0] * (n + 1)

        for i, ch in enumerate(s):
            cnt[i + 1] = cnt[i]
            digit_sum[i + 1] = digit_sum[i]
            if ch != '0':
                cnt[i + 1] += 1
                digit_sum[i + 1] += int(ch)

        # powers of 10
        pw = [1] * (cnt[-1] + 1)
        for i in range(1, len(pw)):
            pw[i] = (pw[i - 1] * 10) % MOD

        # prefix hash of non-zero digits
        pref = [0] * (n + 1)
        seen = 0
        for i, ch in enumerate(s):
            pref[i + 1] = pref[i]
            if ch != '0':
                pref[i + 1] = (pref[i] * 10 + int(ch)) % MOD
                seen += 1

        ans = []

        for l, r in queries:
            total_digits = cnt[r + 1] - cnt[l]
            if total_digits == 0:
                ans.append(0)
                continue

            x = (
                pref[r + 1]
                - pref[l] * pw[total_digits] % MOD
            ) % MOD

            sm = digit_sum[r + 1] - digit_sum[l]
            ans.append((x * sm) % MOD)

        return ans