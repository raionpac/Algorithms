class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None:
            return False
        if node.val == key:
            return True
        elif key < node.val:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)


# Example usage
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)

key_to_find = 15
if bst.search(key_to_find):
    print(f"Key {key_to_find} found in the BST")
else:
    print(f"Key {key_to_find} not found in the BST")
