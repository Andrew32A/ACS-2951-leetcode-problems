# *******************************************************************************
# Question
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example 1:
# Input: board = [["A","B","C","E"]
# ,["S","F","C","S"]
# ,["A","D","E","E"]], word = "ABCCED"
# Output: true

# Example 2:
# Input: board = [["A","B","C","E"]
# ,["S","F","C","S"]
# ,["A","D","E","E"]], word = "SEE"
# Output: true

# *******************************************************************************
# Solution
# The problem can be solved using a backtracking approach. We can iterate through each cell in the grid and perform a depth-first search (DFS) to check if the word can be found starting from that cell.
# The DFS function can be defined as follows:
# 1. Check if the current cell (i, j) is out of bounds or the letter in the cell does not match the current character of the word. In such cases, return False to backtrack.
# 2. If the current character matches the letter in the cell, mark the cell as visited (e.g., by changing the letter to a special character like "#") to avoid reusing it.
# 3. Recursively call the DFS function for the neighboring cells (up, down, left, right) to continue searching for the next character of the word.
# 4. If the word is fully found (i.e., all characters have been matched), return True to indicate a successful path.
# The main function can be defined as follows:
# 1. Iterate through each cell in the grid and call the DFS function to check if the word can be found starting from that cell.
# 2. If the DFS function returns True for any starting cell, it means the word exists in the grid, so we return True.
# 3. If the DFS function returns False for all starting cells, it means the word does not exist in the grid, so we return False.

class Solution(object):
    def exist(self, board, word):
        def dfs(i, j, k):
            if not (0 <= i < m) or not (0 <= j < n) or board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            temp = board[i][j]
            board[i][j] = "#"

            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = i + di, j + dj
                if dfs(ni, nj, k + 1):
                    return True

            board[i][j] = temp
            return False

        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False


# Test case 1
board1 = [["A", "B", "C", "E"],
          ["S", "F", "C", "S"],
          ["A", "D", "E", "E"]]
word1 = "ABCCED"
solution = Solution()
result1 = solution.exist(board1, word1)
print(result1)

# Test case 2
word2 = "SEE"
result2 = solution.exist(board1, word2)
print(result2)


# Time Complexity: O(m * n * 3^k), where m is the number of rows in the grid, n is the number of columns in the grid, and k is the length of the word. In the worst case, for each cell in the grid, the DFS function is called recursively up to 3^k times.
# Space Complexity: O(k), where k is the length of the word. The space is used for the recursive call stack during the DFS traversal.
# Overall, the space complexity is dependent on the length of the word.