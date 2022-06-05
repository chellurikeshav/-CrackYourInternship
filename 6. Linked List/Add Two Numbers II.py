# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dup1,dup2 = l1,l2
        n1,n2 = '',''
        
        while dup1:
            n1 += str(dup1.val)
            dup1 = dup1.next
        
        while dup2:
            n2 += str(dup2.val)
            dup2 = dup2.next
        
        n = str(int(n1)+int(n2))
        len_n = len(n)
        
        l = ListNode()
        pointer = l

        for i in range(len_n):
            l.val = int(n[i])
            
            if i != len_n - 1:
                l.next = ListNode()
                l = l.next
        
        return pointer
            
        
        
        