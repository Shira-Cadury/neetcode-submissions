# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        slow = head
        fast = head
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
            if slow.val == fast.val and slow.next == fast.next:
                return True
        return False        