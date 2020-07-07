# https://www.algoexpert.io/questions/BST%20Construction
# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.

class BST:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):

        # Write your code here.
        # Do not edit the return statement of this method.

        node = self

        while True:
            if value < node.value:
                if node.left == None:
                    node.left = BST(value)
                    break
                else:
                    node = node.left
            else:
                if node.right == None:
                    node.right = BST(value)
                    break
                else:
                    node = node.right
        return self

    def contains(self, value):

        # Write your code here.

        node = self
        while node != None:
            if value < node.value:
                node = node.left
            elif value > node.value:
                node = node.right
            else:
                return True
        return False

    def remove(self, value):

        # Write your code here.
        # Do not edit the return statement of this method.

        node = self
        parent = self
        while node != None:
            if value < node.value:
                parent = node
                node = node.left
            elif value > node.value:
                parent = node
                node = node.right
            else:
                deleteNode = node.right.getMinNode()
                newNode = BST(deleteNode.value)
                parent.right = newNode
                newNode.left = node.left
                newNode.right = node.right
                deleteNode = None
                break
        return self

    def getMinNode(self):
        node = self
        while node.left != None:
            node = node.left
        return node


root = BST(10)
root.left = BST(5)
root.right = BST(15)
root.left.left = BST(2)
root.left.right = BST(3)
root.left.left.left = BST(1)
root.right.left = BST(13)
root.right.right = BST(22)

# root.right.left.left = BST(12)

root.right.left.right = BST(14)
root.right.right.left = BST(21)

root.insert(12)
print(root.right.left.left.value)

print(root.contains(23))

# False

print(root.contains(21))

# True

root.remove(15)
print(root.right.value)

# 21
