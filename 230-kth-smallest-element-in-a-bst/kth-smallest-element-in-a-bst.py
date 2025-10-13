# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # in-order traversal to get all nodes with early exit
        self.counter = 0
        self.k = k
        self.ans = None
        self.inorder(root)

        return self.ans

    
    def inorder(self, node) -> None:
        # process
        if not node:
            return
        
        self.inorder(node.left)
        self.counter += 1
        # done
        if self.counter == self.k:
            self.ans = node.val
            return
        self.inorder(node.right)
