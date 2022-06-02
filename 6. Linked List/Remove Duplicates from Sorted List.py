# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None or head.next==None:
            return head
        
        dup_head = head
        
        prev_val = head.val
        while head.next!= None:
            
            new_head = head.next
            while new_head!= None and new_head.val == prev_val:
                new_head = new_head.next
            try:
                prev_val = new_head.val
                head.next = new_head
                head = head.next
            except:
                head.next = None
            
        return dup_head
            
        
            
            
        