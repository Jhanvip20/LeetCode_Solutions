# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        current = head
        
        while current:

            for _ in range(m - 1):
                if current.next:
                    current = current.next
                else:
                    return head

            deleteCurrent = current

            for _ in range(n):
                if deleteCurrent.next:
                    deleteCurrent = deleteCurrent.next
                else:
                    current.next = None
                    return head

            current.next = deleteCurrent.next
            current = current.next
            
        return head