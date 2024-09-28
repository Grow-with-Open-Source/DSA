# Valid Anagram
Problem Name: 242. Valid Anagram

Approach: Using Hash Maps

Difficulty: Easy

Link: [Leetcode](https://leetcode.com/problems/valid-anagram/description/)

Explanation:

In this problem, we are given two strings, s and t. We need to determine if t is an anagram of s. An anagram is a word or phrase formed by rearranging the letters of another word or phrase, typically using all the original letters exactly once.

Solution Explanation

Check Lengths:
First, check if the lengths of the two strings are equal. If not, return false immediately as they cannot be anagrams.
Count Characters:

Use two hash maps to count the frequency of each character in the strings s and t.
Iterate through the characters of s and update the count in countS.
Similarly, iterate through the characters of t and update the count in countT.
Compare Counts:

Compare the two hash maps. If both maps are identical, then t is an anagram of s.

Examples

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints
1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.