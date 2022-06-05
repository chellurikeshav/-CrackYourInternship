# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dupA,dupB = l1,l2
        l1_high = True
        while dupA or dupB:
            try:
                dupA = dupA.next
            except:
                l1_high = False
                break
            try:
                dupB = dupB.next
            except:
                l1_high = True
                break
        if l1_high:
            temp = l1
            sec = l2
        else:
            temp = l2
            sec = l1
        
        carry = 0
        dup = sec.val
        while temp:
            val = temp.val + dup + carry
            if val>=10:
                temp.val = val%10
                carry = val//10
            else:
                temp.val = val
                carry = 0
                
            if temp.next == None:
                if carry!=0:
                    temp.next = ListNode()
                    temp = temp.next
                    temp.val = carry
                    break
            temp = temp.next
            try:
                sec = sec.next
                dup = sec.val
            except:
                dup = 0
            
        if l1_high:
            return l1
        else:
            return l2
            
            
            
        