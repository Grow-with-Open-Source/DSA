## 3. Linked Lists
A **Linked List** is a linear data structure consisting of nodes, where each node contains a data part and a reference (or link) to the next node in the sequence.

### Key Characteristics
- Nodes are stored non-contiguously in memory.
- Elements are linked using pointers, allowing efficient insertion and deletion.

### Types of Linked Lists
- **Singly Linked List**: Each node has a single link to the next node.
- **Doubly Linked List**: Each node has links to both the previous and next nodes.
- **Circular Linked List**: Last node links back to the first node.

### Common Operations
- **Insertion**:
  - At the head, tail, or a specific position.
  - Complexity: \(O(1)\) for head or tail (if tail pointer exists), \(O(n)\) for arbitrary position.
- **Deletion**:
  - Removing an element from head, tail, or specific position.
  - Complexity: \(O(1)\) for head or tail, \(O(n)\) for arbitrary position.
- **Traversal**: Accessing elements sequentially.
  - Complexity: \(O(n)\)
- **Searching**:
  - Finding an element.
  - Complexity: \(O(n)\)

### Applications
- **Dynamic Memory Management**: Efficient for varying data sizes.
- **Implementing Stacks and Queues**: Using linked lists as the underlying data structure.
- **Sparse Matrices**: Efficiently storing and accessing non-zero elements.
