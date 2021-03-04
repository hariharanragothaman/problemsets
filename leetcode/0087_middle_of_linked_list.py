"""
Problem 876: Middle of linked list

Given a non-empty, singly linked list with head node head, return a middle node of linked list.
If there are two middle nodes, return the second middle node.
"""

# Definition for singly-linked list.abs# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def listLength(self, head: ListNode) -> ListNode:
        flag = 0
        while head != None:
            head = head.next
            flag += 1
        return flag
        
        
    def middleNode(self, head: ListNode) -> ListNode:
        list_length = self.listLength(head)
        print(list_length)
        if list_length % 2 !=0:
            middle_index = (list_length // 2) + 1
        else:
            middle_index = (list_length/2) + 1
        
        flag = 0
        while head != None:
            flag += 1
            if flag == middle_index:
                return head
            
            head = head.next
            
