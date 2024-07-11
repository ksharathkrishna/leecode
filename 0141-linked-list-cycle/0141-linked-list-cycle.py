# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        f = head
        s = head
        
        while f and f.next and f.next.next:
            f = f.next.next
            s = s.next
            if s == f:
                return True
            
        return False