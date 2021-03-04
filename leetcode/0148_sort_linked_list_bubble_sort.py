# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        """
        What sort can we use here?
        We can use - Bubble Sort?

        the idea here is to use swap control.

        """
        if head!= None:
            while(1):
                swap = 0
                tmp = head
                
                while tmp.next != None:
                    if tmp.val > tmp.next.val:
                        tmp.val, tmp.next.val = tmp.next.val, tmp.val
                        tmp = tmp.next
                        swap += 1
                    else:
                        tmp = tmp.next
                
                # Check if swap is zero:
                if swap == 0:
                    break
                else:
                    continue
            return head
        else:
            return head
