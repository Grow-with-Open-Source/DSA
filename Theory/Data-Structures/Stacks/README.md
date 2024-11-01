## 1. Stacks
A **Stack** is a linear data structure that follows the Last-In-First-Out (LIFO) principle. This means the last element added is the first one to be removed.

### Key Characteristics
- Operates in a **LIFO** order.
- Can be implemented using arrays or linked lists.

### Common Operations
- **Push(x)**: Adds element `x` to the top of the stack.
  - Complexity: \(O(1)\)
- **Pop()**: Removes and returns the top element.
  - Complexity: \(O(1)\)
- **Peek/Top()**: Returns the top element without removing it.
  - Complexity: \(O(1)\)
- **isEmpty()**: Checks if the stack is empty.
  - Complexity: \(O(1)\)

### Applications
- **Expression Parsing**: Evaluating postfix and infix expressions.
- **Function Calls**: Recursive calls use a call stack.
- **Backtracking**: Helps in scenarios where previous states are revisited, like maze solving or browser history.
