## 4. Trees
A **Tree** is a hierarchical data structure consisting of nodes with a parent-child relationship. It starts with a **root** node and expands into subtrees of children, representing various hierarchical levels.

### Key Characteristics
- Each node has data and links to child nodes.
- Commonly represented as a **rooted tree** with a single root node.

### Types of Trees
- **Binary Tree**: Each node has at most two children.
- **Binary Search Tree (BST)**: A binary tree with the left child <= root <= right child.
- **Balanced Trees**: Trees like AVL, Red-Black Trees keep balance for efficient operations.
- **Heap**: A complete binary tree used for priority queues.
- **Trie**: A tree for storing strings, useful in search applications.
- **B-Trees**: Balanced trees used in databases and filesystems.

### Common Operations
- **Insertion**:
  - Adds nodes based on tree type (e.g., BST properties).
  - Complexity: \(O(\log n)\) for balanced trees; \(O(n)\) for unbalanced.
- **Deletion**:
  - Removes a node while maintaining tree properties.
  - Complexity: \(O(\log n)\) for balanced trees; \(O(n)\) for unbalanced.
- **Traversal**:
  - **In-order**: Left, Root, Right (BST sorted order).
  - **Pre-order**: Root, Left, Right (used for copying).
  - **Post-order**: Left, Right, Root (used for deletion).
  - Complexity: \(O(n)\)
- **Searching**:
  - Complexity: \(O(\log n)\) for balanced trees; \(O(n)\) for unbalanced.

### Applications
- **Hierarchical Data Representation**: File systems, organizational structures.
- **Binary Search Trees (BSTs)**: Efficient searching, insertion, and deletion.
- **Priority Queues**: Implemented using heaps.
- **Trie**: Used for autocomplete and dictionary implementations.
- **Databases and Filesystems**: B-trees provide efficient data retrieval.
  