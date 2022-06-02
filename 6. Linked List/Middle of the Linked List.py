# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 1
        new_head = head
        while new_head.next != None :
            n = n+1
            new_head = new_head.next
        
        n = n//2
        
        while n!=0:
            head = head.next
            n-=1
        return head
        