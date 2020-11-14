# Remove Zero Sum Consecutive Nodes from Linked List

# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import OrderedDict
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
        prefixNodeMap = OrderedDict()
        
        prefix = 0
        # in case head is removed
        dummy = ListNode(next=head)
        prefixNodeMap[0] = dummy
        cur = dummy.next
        
        while cur:
            prefix = prefix + cur.val
            # check if there's a match from the hashmap
            if prefix in prefixNodeMap:
                prefixNodeMap[prefix].next = cur.next
                
                # nodes that are removed need to be cleared from hashmap
                
                keyList = list(prefixNodeMap.keys())
                for i in range(len(keyList)):
                    if keyList[i] == prefix:
                        i += 1
                        while i < len(keyList): 
                            del prefixNodeMap[keyList[i]]
                            i += 1
                        break
                    
            else:                
            # add to the hashmap            
                prefixNodeMap[prefix] = cur

            cur = cur.next

        return dummy.next


s = Solution()

node = ListNode(1,ListNode(2,ListNode(-3,ListNode(3,ListNode(1)))))

print(s.removeZeroSumSublists(node))

# input [1,3,2,-3,-2,5,5,-5,1]
node1 = ListNode(1,ListNode(3,ListNode(2,ListNode(-3,ListNode(-2,ListNode(5,ListNode(5,ListNode(-5,ListNode(1)))))))))

print(s.removeZeroSumSublists(node1))