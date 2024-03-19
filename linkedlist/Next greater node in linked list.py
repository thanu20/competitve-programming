class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        answer=[]
        stack=[]
        i=0
        h=head
        while h:
            answer.append(0)
            while stack and stack[-1][0]<h.val: 
                value,idx=stack.pop()
                answer[idx]=h.val
            stack.append((h.val,i))
            i+=1
            h=h.next
        return answer 
