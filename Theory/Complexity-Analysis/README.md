# Complexity Analysis

Complexity analysis evaluates the efficiency of algorithms in terms of time and space. The goal is to understand how an algorithm performs as input size grows, using Big O, Big Θ, and Big Ω notations.

## 1. Time Complexity
Time complexity measures the time taken by an algorithm to run as a function of the input size \(n\).

- **Big O (O)**: Upper bound. Worst-case scenario.
- **Big Θ (Θ)**: Tight bound. Average-case scenario.
- **Big Ω (Ω)**: Lower bound. Best-case scenario.

### Common Time Complexities
| Complexity      | Description                          | Example                      |
|-----------------|--------------------------------------|------------------------------|
| **O(1)**        | Constant time                        | Accessing an array element   |
| **O(log n)**    | Logarithmic                          | Binary search                |
| **O(n)**        | Linear                               | Linear search                |
| **O(n log n)**  | Linearithmic                         | Merge sort, heapsort         |
| **O(n^2)**      | Quadratic                            | Bubble sort, insertion sort  |
| **O(2^n)**      | Exponential                          | Recursive Fibonacci          |
| **O(n!)**       | Factorial                            | Permutation generation       |

## 2. Space Complexity
Space complexity measures the amount of memory required by an algorithm as a function of input size.

- Includes both auxiliary space and input space.
- Important for memory-intensive applications.

## 3. Asymptotic Notations
These notations describe the growth rate of functions:

- **Big O (O)**: Upper limit; worst-case behavior.
- **Big Θ (Θ)**: Average or "tight" bound; commonly expected performance.
- **Big Ω (Ω)**: Lower limit; best-case behavior.

## 4. Trade-offs
- **Time vs Space**: Faster algorithms often use more memory, and vice versa.
- **Amortized Analysis**: For operations like dynamic array resizing, considers average time per operation over a sequence.

Understanding complexity is key to choosing the most efficient algorithm for a given problem.
