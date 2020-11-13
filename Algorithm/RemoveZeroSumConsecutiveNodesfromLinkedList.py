# Remove Zero Sum Consecutive Nodes from Linked List

# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        sumIndexMap = {}
        
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        cur = head
        
        while not cur:
            # check if there's a match from the hashmap
            if cur.value in sumIndexMap:
                sumIndexMap[cur.value].next = cur.next
                return dummy.next // in case head is removed
            # add to the hashmap
            else:
                sumIndexMap[-cur.val] = prev

            cur = cur.next
            prev = prev.next

        return dummy.next