class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack=[]
        dummy=headNew=ListNode(None,head)
        curr=head
        while curr:
            while stack and stack[-1].val<curr.val:
                stack.pop()
            stack.append(curr)
            curr=curr.next
        for node in stack:
            headNew.next=node
            headNew=headNew.next
        return dummy.next
