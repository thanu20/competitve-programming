# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        #find the root node using fast and slow pointers where slow becomes root and fast will be a null value
        if not head:
            return None
        def middle(start,end):
            slow=start
            fast=start
            while fast!=end and fast.next!=end:
                slow=slow.next
                fast=fast.next.next
            return slow
        def convert(start,end):
            if start==end:
                return None
            a=middle(start,end)#finding the middle value
            root=TreeNode(a.val)
            root.left=convert(start,a)
            root.right=convert(a.next,end)
            return root
        return convert(head,None)
