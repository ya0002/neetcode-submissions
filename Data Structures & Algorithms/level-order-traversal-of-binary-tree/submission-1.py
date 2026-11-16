# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        level_order = []
        to_extract = [root]

        while to_extract:
            
            to_extract_next = []
            level = []
            for n in to_extract:
                level.append(n.val) ## append nodes of that level
                ## save their children for next iteration/level
                if n.left:
                    to_extract_next.append(n.left)
                if n.right:
                    to_extract_next.append(n.right)
            
            level_order.append(level)
            to_extract = to_extract_next

        return level_order
        