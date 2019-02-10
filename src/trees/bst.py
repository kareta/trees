
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
            elif node.key > current.key:
                current = current.right
            elif node.key <= current.key:
                current = current.left

    def traverse_in_order(self):
        if self.root is None:
            return []

        ordered_nodes = []
        stack = [self.root]
        while stack:
            current = stack.pop()

            if current.left is None:
                ordered_nodes.append(current)

            if current.left is None and current.right is not None:
                stack.append(current.right)
            elif current.left is not None:
                stack.append(current.left)

        return ordered_nodes








