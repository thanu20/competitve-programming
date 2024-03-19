class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack=[]
        dummy=headnew=ListNode(None,head)
        curr=head
        while curr:
            while stack and stack[-1].val<curr.val:
                stack.pop()
            stack.append(curr)
            curr=curr.next
        for node in stack:
            headnew.next=node
            headnew=headnew.next

        return dummy.next
