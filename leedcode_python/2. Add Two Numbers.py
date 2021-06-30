# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2 ):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if(l1 == None):
            return l2
        if(l2 == None):
            return l1
            
        l1.val = l1.val + l2.val
        if(l1.val >= 10):
            l1.val = l1.val % 10
            if(l1.next != None):
                l1.next.val = l1.next.val + 1
            else: 
                l1.next = ListNode()
                l1.next.val = 1
                
        l1.next = self.addTwoNumbers(l1.next , l2.next,)
        
        return l1