# Maximum Depth of Binary Tree
# description: https://leetcode.com/problems/maximum-depth-of-binary-tree/


######################  version 1  ######################
# try version 1 in your favorite python IDE
from queue import deque

class Node(object):
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    # DFS: recursive
    def dfs(self):
        if self.left != None:
            left = self.left.dfs()
        else:
            left = 0
        if self.right != None:
            right = self.right.dfs()
        else:
            right = 0

        return max(left, right) + 1

    # DFS: iterative
    def dfsIterative(self):
        stack = [[self, 1]]
        maxDepth = 0
        while len(stack):
            [node, depth] = stack.pop()
            maxDepth = max(maxDepth, depth)

            if node.left != None:
                stack.append([node.left, depth + 1])
            if node.right != None:
                stack.append([node.right, depth + 1])
        return maxDepth

    # BFS: iterative
    def bfs(self):
        queue = deque([self])
        depth = 0
        while len(queue):
            size = len(queue)
            depth += 1
            for i in range(size):
                node = queue.popleft()
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
        return depth


#     a
#    / \
#   b   c
#  / \   \
# d   e   f

root = Node('a', [Node('b', [Node('d'), Node('e')]), Node('c', [Node('f')])])

#     a
#    / \
#   b   c
#    \   \
#    d   e
#         \
#         f
root = Node('a')
root.left = Node('b')
root.right = Node('c')
root.left.right = Node('d')
root.right.right = Node('e')
root.right.right.right = Node('f')

print(root.dfs())
# 4
print("")

print(root.dfsIterative())
# 4
print("")

print(root.bfs())
# 4

######################  version 2  ######################
# try version 2 in leetcode IDE: https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import deque

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
    #   return self.dfs(root)
    #   return self.dfsIterative(root)
        return self.bfs(root)


    # DFS: recursive
    def dfs(self, node):
        if node != None:
            if node.left != None:
                left = self.dfs(node.left)
            else:
                left = 0
            if node.right != None:
                right = self.dfs(node.right)
            else:
                right = 0
        else:
            return 0

        return max(left, right) + 1

    # DFS: iterative
    def dfsIterative(self, node):
        if node != None:
            stack = [[node,1]]
            maxDepth = 0
            while len(stack):
                [node, depth] = stack.pop()
                maxDepth = max(maxDepth, depth)

                if node.left != None:
                    stack.append([node.left, depth + 1])
                if node.right != None:
                    stack.append([node.right, depth + 1])
        else:
            return 0
        return maxDepth

    # BFS: iterative
    def bfs(self, node):
        if node != None:
            queue = deque([node])
            depth = 0
            while len(queue):
                size = len(queue)
                depth += 1

                for i in range(size):
                    node = queue.popleft()
                    if node.left != None:
                        queue.append(node.left)
                    if node.right != None:
                        queue.append(node.right)
        else:
            return 0
        return depth
