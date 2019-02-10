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


def test_it_traverses_a_tree_in_order():
    tree = BinarySearchTree()
    keys = [50, 25, 30, 15, 100, 75, 56]
    for key in keys:
        node = Node(key)
        tree.add(node)

    expected = [15, 25, 30, 50, 56, 75, 100]
    ordered_nodes = tree.traverse_in_order()
    for index, node in enumerate(ordered_nodes):
        assert expected[index] == node.key
