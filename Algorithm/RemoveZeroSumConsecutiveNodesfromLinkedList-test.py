# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        cur = self
        output = ''

        while cur:
            output = output + str(cur.val) + ' '
            cur = cur.next
        return output
    
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        prefixNodeMap = {}
        
        prefix = 0
        dummy = ListNode()
        dummy.next = head
        prefixNodeMap[0] = dummy
        cur = dummy.next
        
        while cur:
            prefix = prefix + cur.val
            
            if prefix in prefixNodeMap:
                prefixNodeMap[prefix].next = cur.next
            else:                
                prefixNodeMap[prefix] = cur

            cur = cur.next

        return dummy.next


s = Solution()

node = ListNode(1,ListNode(2,ListNode(-3,ListNode(3,ListNode(1)))))

print(s.removeZeroSumSublists(node))

