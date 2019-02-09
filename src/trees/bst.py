
class Node:
    def __init__(self, key, left=None, right=None):
        self.left = left
        self.right = right
        self.key = key


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, node):
        if self.root is None:
            self.root = node
            return

        current = self.root
        while True:
            if node.key > current.key and current.right is None:
                current.right = node
                return
            elif node.key <= current.key and current.left is None:
                current.left = node
                return
            elif node > current.key:
                current = current.right
            elif node <= current.key:
                current = current.left
