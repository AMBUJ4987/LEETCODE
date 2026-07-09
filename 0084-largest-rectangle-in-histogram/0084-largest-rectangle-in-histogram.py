class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []       
        ans = 0
        n = len(heights)

        for i in range(n + 1):
            curr = 0 if i == n else heights[i]

            while stack and heights[stack[-1]] > curr:
                h = heights[stack.pop()]
                left = stack[-1] if stack else -1
                width = i - left - 1
                ans = max(ans, h * width)

            stack.append(i)

        return ans