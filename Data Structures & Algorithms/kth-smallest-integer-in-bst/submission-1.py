# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    
    def inorder(self,node,s,k):

        if node.left:
            self.inorder(node.left,s,k)
        
        
        if len(s)==k:
            return s
        s.append(node.val)

        if node.right:
            self.inorder(node.right,s,k)
        return s
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        
        s = self.inorder(root,[],k)
        print(s)

        return s[k-1]




        