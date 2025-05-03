# 2023.06.10

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# TreeNode{val: 1, left: None, right: TreeNode{val: 2, left: TreeNode{val: 3, left: None, right: None}, right: None}}

from types import List, Optional

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        def traversalNode(node: TreeNode):
            if node is not None:
                traversalNode(node.left)
                ret.append(node.val)
                traversalNode(node.right)
        traversalNode(root)
        return ret
            






