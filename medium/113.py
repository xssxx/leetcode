# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        path = []
        curr = 0

        def dfs(node):
            nonlocal curr, path, ans
            if node is None:
                return

            # print(node.val)
            path.append(node.val)
            curr += node.val

            if curr == targetSum and node.left is None and node.right is None:
                ans.append(path.copy())

            # print(path)
            # print(curr)

            dfs(node.left)
            dfs(node.right)

            curr -= path[-1]
            path.pop()

        dfs(root)
        # print(ans)
        return ans
