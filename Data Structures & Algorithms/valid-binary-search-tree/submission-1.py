# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def valid(self,node,left,right):

        if not node:
            return True
        
        if not (node.val>left and node.val<right):
            return False
        
        return (self.valid(node.left,left,node.val) and 
        self.valid(node.right,node.val,right))
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        return self.valid(root,float("-inf"),float("inf"))
        
        # if not root:
        #     return True
        # print(vars(root))
        # return (
        #     ((root.left and root.val>root.left.val and self.isValidBST(root.left)) or (not root.left)) and 
        #     ((root.right and root.val<root.right.val and self.isValidBST(root.right)) or (not root.right))
        # )
        

        