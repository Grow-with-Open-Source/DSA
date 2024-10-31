#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;

// Function to find the length of the longest substring without repeating characters
int lengthOfLongestSubstring(const string &s) {
    unordered_map<char, int> charIndexMap;
    int maxLength = 0;
    int start = 0;

    for (int end = 0; end < s.length(); end++) {
        char currentChar = s[end];
        
        // If the character is already in the map and is within the current window
        if (charIndexMap.find(currentChar) != charIndexMap.end() && charIndexMap[currentChar] >= start) {
            start = charIndexMap[currentChar] + 1;
        }
        
        // Update the last seen index of the current character
        charIndexMap[currentChar] = end;
        
        // Calculate the max length of substring
        maxLength = max(maxLength, end - start + 1);
    }
    return maxLength;
}

int main() {
    string input;
    cout << "Enter a string: ";
    cin >> input;

    int result = lengthOfLongestSubstring(input);
    cout << "The length of the longest substring without repeating characters is: " << result << endl;

    return 0;
}

/*
Example:
Input: "abcabcbb"
Explanation:
- The longest substring without repeating characters is "abc", which has a length of 3.
- As we iterate through the string:
    - Start with "a" -> length 1
    - Add "b" -> "ab" -> length 2
    - Add "c" -> "abc" -> length 3
    - "a" repeats, so move the start to the next character -> "bca" (length still 3)
    - Continue until the end, with the longest substring remaining "abc".
Output: 3

Input: "bbbbb"
Explanation:
- The longest substring without repeating characters is "b", which has a length of 1.
Output: 1
*/
