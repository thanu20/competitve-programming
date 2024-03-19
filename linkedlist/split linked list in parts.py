class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length=0
        temp=head
        while temp:
            length+=1
            temp=temp.next
        width,remainder=divmod(length,k)
        result,current=[],head
        for i in range(k):
            dummy=write=ListNode(0)
            for j in range(width+(i<remainder)):
                if current:
                    write.next=write=ListNode(current.val)
                    current=current.next
            result.append(dummy.next)
        return result
