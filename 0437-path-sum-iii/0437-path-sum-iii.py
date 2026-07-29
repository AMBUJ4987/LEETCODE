from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root, targetSum):
        if not root:
            return 0

        ans = 0

        def dfs(node, curr_sum):
            nonlocal ans
            if not node:
                return 0

            curr_sum += node.val

            if curr_sum == targetSum:
                ans += 1

            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)

        q = deque([root])

        while q:
            node = q.popleft()

            dfs(node, 0)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return ans