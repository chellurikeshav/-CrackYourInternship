# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        n = 0
        new_head = head
        while new_head.next!=None:
            n+=1
            new_head = new_head.next
        
        result = head.val*(2**(n))
        
        while head.next!=None:
            head = head.next
            n = n-1
            result+= (head.val)*(2**(n))
        
        return result