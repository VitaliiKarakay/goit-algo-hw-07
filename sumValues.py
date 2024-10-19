from binarySearchTree import BinarySearchTree


def sum_values(node):
    if node is None:
        return 0
    return node.value + sum_values(node.left) + sum_values(node.right)


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)
    print("Sum of all values:", sum_values(bst.root))