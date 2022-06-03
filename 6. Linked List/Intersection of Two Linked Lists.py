# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA == None and headB == None:
            return None
        c = {}
        
        while headA:
            c[headA] = 'Present'
            headA = headA.next
        
        while headB:
            if headB in c:
                return headB
            headB = headB.next
        
        return None
                