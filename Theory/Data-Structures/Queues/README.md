## 2. Queues
A **Queue** is a linear data structure that follows the First-In-First-Out (FIFO) principle. The first element added is the first to be removed.

### Key Characteristics
- Operates in a **FIFO** order.
- Can be implemented using arrays, linked lists, or circular buffers.

### Types of Queues
- **Simple Queue**: Basic FIFO queue.
- **Circular Queue**: The last position is connected back to the first.
- **Priority Queue**: Elements are dequeued based on priority.
- **Deque**: Double-ended queue, allowing insertion and deletion at both ends.

### Common Operations
- **Enqueue(x)**: Adds element `x` at the end of the queue.
  - Complexity: \(O(1)\)
- **Dequeue()**: Removes and returns the front element.
  - Complexity: \(O(1)\)
- **Front()**: Returns the front element without removing it.
  - Complexity: \(O(1)\)
- **isEmpty()**: Checks if the queue is empty.
  - Complexity: \(O(1)\)

### Applications
- **CPU Scheduling**: Round-robin scheduling.
- **Breadth-First Search (BFS)**: Used in graph traversal.
- **IO Buffers**: Handling asynchronous data.
