# *******************************************************************************
# Question
# Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the answer in any order.
# A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

# Example 1:
# Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
# Output: ["mee","aqq"]
# Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}.
# "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation, since a and b map to the same letter.

# Example 2:
# Input: words = ["a","b","c"], pattern = "a"
# Output: ["a","b","c"]

# *******************************************************************************
# Solution
# The problem can be solved by checking each word in the list against the given pattern. For each word, we can create two dictionaries to map the characters in the pattern to the corresponding characters in the word, and vice versa.
# The solution can be defined as follows:
# 1. Initialize an empty result list.
# 2. Iterate through each word in the words list.
# 3. Create two empty dictionaries: pattern_to_word and word_to_pattern.
# 4. Check if the length of the word matches the length of the pattern. If not, skip to the next word.
# 5. Iterate through each character and its corresponding index in the pattern.
# - If the character is already in the pattern_to_word dictionary and its corresponding character in the word does not match the mapped value, or if the character is already in the word_to_pattern dictionary and its corresponding character in the pattern does not match the mapped value, break the loop and skip to the next word.
# - Otherwise, add the character and its corresponding character in the word to the pattern_to_word and word_to_pattern dictionaries, respectively.
# 6. If the loop completes without breaking, it means the word matches the pattern. Add the word to the result list.
# 7. After iterating through all the words, return the result list.

class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        result = []
        for word in words:
            pattern_to_word = {}
            word_to_pattern = {}
            
            if len(word) != len(pattern):
                continue
            
            for i, char in enumerate(pattern):
                if char in pattern_to_word and pattern_to_word[char] != word[i]:
                    break
                if word[i] in word_to_pattern and word_to_pattern[word[i]] != char:
                    break
                
                pattern_to_word[char] = word[i]
                word_to_pattern[word[i]] = char
            else:
                result.append(word)
        
        return result


# Test case 1
words1 = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
pattern1 = "abb"
solution = Solution()
result1 = solution.findAndReplacePattern(words1, pattern1)
print(result1)

# Test case 2
words2 = ["a", "b", "c"]
pattern2 = "a"
result2 = solution.findAndReplacePattern(words2, pattern2)
print(result2)

# Time Complexity: O(N * M), where N is the number of words in the words list and M is the length of the pattern.
# Space Complexity: O(M), where M is the length of the pattern.
