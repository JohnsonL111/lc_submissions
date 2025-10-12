# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # queue
        if not root:
            return []
        q = deque([root])
        res = []

        while q:
            # calculate length of level
            level_size = len(q)
            level_nodes = []

            # do by level
            for _ in range(level_size):

                # process
                node = q.popleft()
                level_nodes.append(node.val)

                # get children
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            # add the level
            res.append(level_nodes)
                
        return res
            




        