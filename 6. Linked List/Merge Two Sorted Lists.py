# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        if list1 == None and list2 == None:
            return None
        
        if list1 == None:
            return list2
        
        if list2 == None:
            return list1
        
        ret_list = sorted_list = ListNode()
        while list1 or list2:

            sorted_list.next = ListNode()
            sorted_list = sorted_list.next
            
            if list1 != None and list2==None:
                sorted_list.val = list1.val
                list1 = list1.next
            
            elif list2 != None and list1==None:
                sorted_list.val = list2.val
                list2 = list2.next
                
            else:
                if list1 and list1.val<=list2.val:
                    sorted_list.val = list1.val
                    list1 = list1.next
                else:
                    sorted_list.val = list2.val
                    list2 = list2.next
        
        return ret_list.next
                
                