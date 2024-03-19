# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        size = lambda node: 0 if not node else 1 + size(node.next)
        total_size = size(root)
        part_size, remainder = divmod(total_size, k)
        parts = [None] * k
        prev = None
        for i in range(k):
            parts[i], prev = root, root
            for _ in range(part_size + (i < remainder)):
                prev, root = root, root.next
            if prev:
                prev.next = None
        return parts
