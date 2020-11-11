# Linked List in Binary Tree
# https://leetcode.com/problems/linked-list-in-binary-tree/

# Case not passed
# Input: [1,10] [1,null,1,10,1,9] Output: false

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if head == None:
            return True
        if root == None:
            return False
        
        if head.val == root.val:
            return self.matchedContinue(head.next, root.left) \
                or self.matchedContinue(head.next, root.right)
        else:
            return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
    
    def matchedContinue(self, listNode: ListNode, treeNode: TreeNode) -> bool:
        if listNode == None and treeNode == None:
            return True
        elif treeNode == None:
            return False
        elif listNode == None:
            return True
            
        if listNode.val == treeNode.val:
            return self.matchedContinue(listNode.next, treeNode.left) \
                or self.matchedContinue(listNode.next, treeNode.right)
        else:
            return False