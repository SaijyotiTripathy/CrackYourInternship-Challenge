# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start,mid=head,head
        
        while mid and mid.next:    #O(n)
            start=start.next
            mid=mid.next.next
        
        return start