from trees.bst import Node, BinarySearchTree


def test_it_creates_a_node():
    node = Node(10)
    assert node.key == 10


def test_it_adds_a_node_as_a_root():
    tree = BinarySearchTree()
    node = Node(10)
    tree.add(node)
    assert tree.root is node


def test_it_adds_a_node_as_a_left_child():
    tree = BinarySearchTree()
    root = Node(10)
    tree.add(root)
    node = Node(5)
    tree.add(node)
    assert tree.root.left is node


def test_it_adds_a_node_as_a_right_child():
    tree = BinarySearchTree()
    root = Node(10)
    tree.add(root)
    node = Node(15)
    tree.add(node)
    assert tree.root.right is node

