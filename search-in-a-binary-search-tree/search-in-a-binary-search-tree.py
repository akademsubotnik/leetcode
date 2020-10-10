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
        #Use the pre-order traversal process which you used in the mergeTrees problem (root->left subtree->right subtree)
        
        t = root 
        t_t = root
        #print t.val

        #If val is less than root.val -> to left subtree, set root = node left of the root node, check again is val less than root.val if yes, move to left subtree, set root = node left of root node, check again, is val less than root.val if no move to right subtree, set root = node right of root node, check again.  repeat until val = root.val or you reach no next node
        
        while t != None :
            print t.val
            if val == t.val :
                print "val found"
                print t
                return t
            if val < t.val :
                #Move to left subtree
                print "Moving to left subtree"
                t = t.left
            elif val > t.val :
                #Move to right subtree
                print "Moving to right subtree"
                t = t.right
            
            
        
        
