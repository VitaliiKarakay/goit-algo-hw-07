from binarySearchTree import BinarySearchTree


def find_max(node):
    if node is None:
        raise ValueError("The tree is empty")

    current = node
    while current.right is not None:
        current = current.right
    return current.value


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(110)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)
    print(find_max(bst.root))