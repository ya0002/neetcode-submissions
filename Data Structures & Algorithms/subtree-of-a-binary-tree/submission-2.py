# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    def is_identical_tree(self, first_node, second_node):
            # If both nodes are null, both trees match up to this point
            if not first_node and not second_node:
                return True
            
            # If one is null and the other is not, their structures differ
            if not first_node or not second_node:
                return False
            
            # Values must be equal, and left and right subtrees must both match identically
            return (first_node.val == second_node.val and 
                    self.is_identical_tree(first_node.left, second_node.left) and 
                    self.is_identical_tree(first_node.right, second_node.right))

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not subRoot:
            return True
        
        if not root:
            return False

        if self.is_identical_tree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        

        
        