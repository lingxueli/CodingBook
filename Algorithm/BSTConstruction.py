# https://www.algoexpert.io/questions/BST%20Construction

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
        
        return self
