# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        if head == None:
            return head
        
        dup = head
        
        while dup and dup.val == val:
            dup = dup.next
        head = prev_node = dup
        
        while dup:
            if dup.val == val:
                prev_node.next = dup.next
            else:
                prev_node = dup
            dup = dup.next
        return head
        