public class Main {
    public static void main(String[] args) {
        // Creating a new instance of BinarySearchTree
        BinarySearchTree bst = new BinarySearchTree();

        // Inserting nodes into the binary search tree
        bst.insert(50);
        bst.insert(30);
        bst.insert(20);
        bst.insert(40);
        bst.insert(70);
        bst.insert(60);
        bst.insert(80);

        // Checking if certain keys are present in the tree
        //System.out.println("Is 6 in the tree? " + bst.containsNode(6));
        //System.out.println("Is 1 in the tree? " + bst.containsNode(1));

        System.out.println("Binary Tree:");
        bst.printTree();

        int keyToFind = 30;
        if (bst.containsNode(keyToFind))
            System.out.println("\nKey " + keyToFind + " found in the Binary Search Tree ");
        else
            System.out.println("\nKey " + keyToFind + " not found in the Binary Search Tree ");
    }
}
