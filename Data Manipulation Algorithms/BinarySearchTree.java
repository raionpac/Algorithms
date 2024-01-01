public class BinarySearchTree {

    Node root; // Root node of the binary search tree

    // Constructor for creating an empty binary search tree
    public BinarySearchTree() {
        root = null;
    }

    // Public method to insert a new key in the BST
    public void insert(int key) {
        root = insertRecursive(root, key);
    }

    // Helper method to insert a new key in the BST recursively
    private Node insertRecursive(Node current, int key) {
        // Base case: if the current node is null, a new node is created
        if (current == null) {
            return new Node(key);
        }

        // Insert in the left subtree if the key is less than current node's key
        if (key < current.key) {
            current.left = insertRecursive(current.left, key);
        }
        // Insert in the right subtree if the key is greater than current node's key
        else if (key > current.key) {
            current.right = insertRecursive(current.right, key);
        }

        // Return the (unchanged) current node
        return current;
    }

    // Public method to search for a key in the BST
    public boolean containsNode(int key) {
        return containsNodeRecursive(root, key);
    }

    // Helper method to search for a key in the BST recursively
    private boolean containsNodeRecursive(Node current, int key) {
        // Base case: if the current node is null, the key is not found
        if (current == null) {
            return false;
        }

        // If the key matches the current node's key, return true
        if (key == current.key) {
            return true;
        }

        // Search in the left subtree if the key is less than the current node's key
        // Otherwise, search in the right subtree
        return key < current.key
                ? containsNodeRecursive(current.left, key)
                : containsNodeRecursive(current.right, key);
    }

    // Function to print binary tree in 2D
    void printTree(Node root, int space, int COUNT) {
        if (root == null)
            return;

        space += COUNT;

        printTree(root.right, space, COUNT);

        System.out.print("\n");
        for (int i = COUNT; i < space; i++)
            System.out.print(" ");
        System.out.print(root.key + "\n");

        printTree(root.left, space, COUNT);
    }

    // Wrapper over printTree
    void printTree() {
        printTree(this.root, 0, 5);
    }

}
