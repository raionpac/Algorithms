public class Node {
    int key;       // The value or key of the node
    Node left;     // Pointer to the left child node
    Node right;    // Pointer to the right child node

    // Constructor to create a new node with a given key
    public Node(int item) {
        key = item;
        left = right = null;
    }
}
