# Traversing two trees in parallel.

# To solve the problem like:
# Are two trees copies of each other?
# Is there a node in one tree that is considered the same as a node in another tree?


class Node:
  def __init__(self, value=None, children=[]):
    self.value = value
    self.children = children

  def prettyPrint(self):
    print self.value
    for child in self.children:
      child.prettyPrint()

  def isClone(self, n2):
    if self.value != n2.value:
      return False
    if len(self.children) != len(n2.children):
      return False
    for i in range(0, len(self.children)):
      if not self.children[i].isClone(n2.children[i]):
        return False
    return True

  def isCloneIterative(self, n2):
    stack = [ (self, n2) ]
    while len(stack):
      (c1, c2) = stack.pop()
      if c1.value != c2.value:
        return False
      if len(c1.children) != len(c2.children):
        return False
      for i in range(0, len(c1.children)):
        stack.append( (c1.children[i], c2.children[i]) )
    return True

#    1
#   / \
#  2   3
# / \
#4   5
n = Node(1)
n.children = [Node(2), Node(3)]
n.children[0].children = [Node(4), Node(5)]

n2 = Node(1)
n2.children = [Node(2), Node(3)]
n2.children[0].children = [Node(4), Node(5)]

print n.isClone(n2)
print n.isCloneIterative(n2)
