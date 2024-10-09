# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p or not q or p.val != q.val :
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        # head1,head3=p,p
        # head2,head4=q,q
        # # flag = True
        # while(head1 and head2):
        #     if (head1.val != head2.val) or (head1.left != head2.left) :
        #         return False
        #     head1=head1.left
        #     head2=head2.left
        # while(head3 and head4):
        #     if (head3.val != head4.val) or (head3.right != head4.right) :
        #         return False
        #     head3=head3.right
        #     hea4=head4.right
        # if head3 is None and head4 is None:
        #     return True