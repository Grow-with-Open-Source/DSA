Problem Name: 844.Backspace String Compare

Approach: Using Stacks

Difficulty: Easy

Link: https://leetcode.com/problems/backspace-string-compare/


Explanation:

In this problem, we are given two strings, s and t, where '#' represents a backspace character. We need to determine if these two strings are equal after simulating the backspace characters.

Here's the explanation of the provided solution:

Create two stacks, s1 and s2, to process the input strings s and t, respectively.

Loop through the characters in string s:

If the character is '#':
Check if s1 is not empty, and if so, pop the top character to simulate backspacing.
Continue to the next character in s.
Otherwise, push the character onto the s1 stack.
Repeat the same process for string t by looping through its characters and pushing or popping as needed, simulating the backspace characters on stack s2.

Create two empty strings, res1 and res2, to store the processed strings after backspacing.

While stack s1 is not empty, pop each character and append it to the res1 string.

Similarly, while stack s2 is not empty, pop each character and append it to the res2 string.

Finally, check if res1 and res2 are equal. If they are equal, return true; otherwise, return false.

The idea behind this solution is to use stacks to simulate the backspace operations for both input strings. After simulating the backspaces, the strings res1 and res2 will contain the characters after backspacing. If these processed strings are equal, the function returns true, indicating that the original strings s and t are the same after backspacing.

Let's walk through an example:

Example:
Input: s = "ab#c", t = "ad#c"

After processing s:
s1 = ['a', 'c']
After processing t:
s2 = ['a', 'c']
Processed strings:
res1 = "ca"
res2 = "ca"
Since res1 and res2 are equal, the function returns true.
Example 2:
Input: s = "ab##", t = "c#d#"

After processing s:
s1 = []
After processing t:
s2 = []
Processed strings:
res1 = ""
res2 = ""
Since res1 and res2 are equal, the function returns true.
Example 3:
Input: s = "a#c", t = "b"

After processing s:
s1 = ['c']
After processing t:
s2 = ['b']
Processed strings:
res1 = "c"
res2 = "b"
Since res1 and res2 are not equal, the function returns false.
