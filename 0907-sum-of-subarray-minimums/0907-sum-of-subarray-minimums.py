class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)

        left = [0] * n
        right = [0] * n

        stack = []

        # Previous Less Element
        for i in range(n):
            count = 1
            while stack and arr[i] <= stack[-1][0]:
                count += stack[-1][1]
                stack.pop()

            stack.append((arr[i], count))
            left[i] = count

        stack = []

        # Next Less Element
        for i in range(n - 1, -1, -1):
            count = 1
            while stack and arr[i] < stack[-1][0]:
                count += stack[-1][1]
                stack.pop()

            stack.append((arr[i], count))
            right[i] = count

        ans = 0
        for i in range(n):
            ans = (ans + arr[i] * left[i] * right[i]) % MOD

        return ans