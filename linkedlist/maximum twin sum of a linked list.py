class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast=slow=head
        stack=[]
        max_twin_sum=0
        while fast and fast.next:
            fast=fast.next.next
            stack.append(slow)
            slow=slow.next
        while slow:
            max_twin_sum=max(max_twin_sum,stack.pop().val+slow.val)
            slow=slow.next
        return max_twin_sum
