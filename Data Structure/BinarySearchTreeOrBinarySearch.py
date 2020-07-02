class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def inorder(node):
  if not node:
    return
  inorder(node.left)
  print(node.val)
  inorder(node.right)

def preorder(node):
  if not node:
    return
  print(node.val)
  preorder(node.left)
  preorder(node.right)

def search(node, key):
  if node is None or node.val == key:
    return node
  if node.val < key:
    return search(node.right, key)
  else:
    return search(node.left, key)


#          4
#         / \
#        2   6
#       / \   \
#      1   3   7
#
node = Node(4, Node(2, Node(1), Node(3)), Node(6, None, Node(7)))
inorder(node)
# 1 2 3 4 5 6 7

preorder(node)
# 4 2 1 3 7 6

print(search(node, 6).val)
# 6
print(search(node, 9))
# None


def binarySearch(nums, low, high, x):
  if high < low:
    return None
  mid = (low + high)//2
  if nums[mid] == x:
    return mid
  elif nums[mid] > x:
    return binarySearch(nums, low, mid-1, x)
  else:
    return binarySearch(nums, mid+1, high, x)

nums = [1, 2, 3, 4, 5, 6, 7, 8]
print(binarySearch(nums, 0, len(nums) - 1, 4))
# 3
print(binarySearch(nums, 0, len(nums) - 1, 40))
# None
