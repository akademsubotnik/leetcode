# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        
        t = root 

        #If val is less than root.val -> to left subtree, set root = node left of the root node, check again is val less than root.val if yes, move to left subtree, set root = node left of root node, check again, is val less than root.val if no move to right subtree, set root = node right of root node, check again.  repeat until val = root.val or you reach no next node
        
        while t != None :
            if val == t.val :
                return t
            elif val < t.val :
                #Move to left subtree
                t = t.left
            elif val > t.val :
                #Move to right subtree
                t = t.right
