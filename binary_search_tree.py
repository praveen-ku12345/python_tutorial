class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.key, end=' ')
        inorder_traversal(root.right)

def preorder_traversal(root):
    if root:
        print(root.key, end=' ')
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.key, end=' ')

def search(root, key):
    if root is None or root.key == key:
        return root
    if key < root.key:
        return search(root.left, key)
    return search(root.right, key)

def delete_node(root, key):
    if root is None:
        return root

    if key < root.key:
        root.left = delete_node(root.left, key)
    elif key > root.key:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        root.key = min_value_node(root.right)
        root.right = delete_node(root.right, root.key)
    return root

def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current.key

def display_tree(root, level=0, prefix="Root: "):
    if root:
        print(" " * (level * 4) + prefix + str(root.key))
        if root.left or root.right:
            display_tree(root.left, level + 1, "L--- ")
            display_tree(root.right, level + 1, "R--- ")

def height_of_tree(root):
    if root is None:
        return 0
    left_height = height_of_tree(root.left)
    right_height = height_of_tree(root.right)
    return max(left_height, right_height) + 1
root = None
while True:
    print("\nBinary Search Tree Operations:")
    print("1. Insert Node")
    print("2. Inorder Traversal")
    print("3. Preorder Traversal")
    print("4. Postorder Traversal")
    print("5. Search Node")
    print("6. Delete Node")
    print("7. Display Tree")
    print("8. Height of Tree")
    print("9. Exit")

    choice = int(input("Enter your choice (1-9): "))

    if choice == 1:
        key = int(input("Enter key to insert: "))
        root = insert(root, key)
    elif choice == 2:
        print("Inorder Traversal:")
        inorder_traversal(root)
    elif choice == 3:
        print("Preorder Traversal:")
        preorder_traversal(root)
    elif choice == 4:
        print("Postorder Traversal:")
        postorder_traversal(root)
    elif choice == 5:
        search_key = int(input("Enter key to search: "))
        if search(root, search_key):
            print(f"Key {search_key} found in the tree.")
        else:
            print(f"Key {search_key} not found in the tree.")
    elif choice == 6:
        delete_key = int(input("Enter key to delete: "))
        root = delete_node(root, delete_key)
        print(f"Key {delete_key} deleted from the tree.")
    elif choice == 7:
        print("Displaying Tree:")
        display_tree(root)
    elif choice == 8:
        print("Height of Tree:", height_of_tree(root))
    elif choice == 9:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
