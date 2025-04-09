# 290. Word Pattern
# Solved
# Easy
# Topics
# Companies
# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.
 

# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"

# Output: true

# Explanation:

# The bijection can be established as:

# 'a' maps to "dog".
# 'b' maps to "cat".
# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"

# Output: false

# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"

# Output: false


class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        string_list = s.split()
        patterndict = dict()
        if len(pattern) != len(s.split()):
            return False
        if len(set(pattern)) != len(set(s.split())):
            return False
        for p in range(len(pattern)):
            if pattern[p] not in patterndict:
                patterndict[pattern[p]] = string_list[p]
            elif pattern[p] in patterndict:
                if patterndict[pattern[p]] != string_list[p]:
                    return False
        return True
                
        