# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        # t tree is subtree
        # if t is null, return True (bc it's subtree of S)
        if not t: return True
        # if s is empty but t is non empty
        if not s and t: return False
        if self.sameTree(s,t):
            return True

        return (self.isSubtree(s.left,t) or
        self.isSubtree(s.right,t))    
    def sameTree (self,s,t):
        # if given empty trees (both null->same tree)
        if not s and not t:
            return True
        #if not both empty, then compare them
        if s and t and s.val==t.val:
            return(self.sameTree(s.left,t.left) and
            self.sameTree(s.right,t.right))
        # if one is empty, one is non empty, return false
        return False
            