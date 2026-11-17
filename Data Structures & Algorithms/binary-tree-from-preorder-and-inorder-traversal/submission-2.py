# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
 
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder or not inorder:
            return None
        
        indices = {val: idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0

        def dfs(l,r):
            if l>r:
                return None
            
            head = TreeNode(val=preorder[self.pre_idx])
            mid = indices[preorder[self.pre_idx]]
            self.pre_idx +=1

            head.left = dfs(l,mid-1)
            head.right = dfs(mid+1,r)

            return head
        
        return dfs(0,len(inorder)-1)


        

        # head = TreeNode(val=preorder[pre_idx])
        # mid = indices[preorder[pre_idx]]

        # head.left=self.buildTree(preorder[1:mid+1],inorder[:mid])
        # head.right=self.buildTree(preorder[mid+1:],inorder[mid+1:])

        # return head
        