# *******************************************************************************
# Question
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# 1. Each row must contain the digits 1-9 without repetition.
# 2. Each column must contain the digits 1-9 without repetition.
# 3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# Note:
# - A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# - Only the filled cells need to be validated according to the mentioned rules.

# Example 1:
# Input: board = [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true

# Example 2:
# Input: board = [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8.
# Since there are two 8's in the top left 3x3 sub-box, it is invalid.

# *******************************************************************************
# Solution
# The problem can be solved using the following steps:
# 1. Create three sets: rowSet, colSet, and boxSet to keep track of the numbers seen in each row, column, and 3x3 sub-box.
# 2. Iterate through each cell in the Sudoku board.
# 3. For each cell, check if the value is already present in the corresponding rowSet, colSet, or boxSet.
# 4. If the value is already present, return False as it violates the Sudoku rules.
# 5. If the value is not present, add it to the corresponding sets.
# 6. After iterating through all the cells, return True, as the board is valid according to the Sudoku rules.

class Solution(object):
    def isValidSudoku(self, board):
        rowSet = [set() for _ in range(9)]
        colSet = [set() for _ in range(9)]
        boxSet = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = board[i][j]
                    boxIndex = (i // 3) * 3 + j // 3

                    if num in rowSet[i] or num in colSet[j] or num in boxSet[boxIndex]:
                        return False

                    rowSet[i].add(num)
                    colSet[j].add(num)
                    boxSet[boxIndex].add(num)

        return True


# Test case 1
board1 = [["5","3",".",".","7",".",".",".","."],
          ["6",".",".","1","9","5",".",".","."],
          [".","9","8",".",".",".",".","6","."],
          ["8",".",".",".","6",".",".",".","3"],
          ["4",".",".","8",".","3",".",".","1"],
          ["7",".",".",".","2",".",".",".","6"],
          [".","6",".",".",".",".","2","8","."],
          [".",".",".","4","1","9",".",".","5"],
          [".",".",".",".","8",".",".","7","9"]]
solution = Solution()
result1 = solution.isValidSudoku(board1)
print(result1)

# Test case 2
board2 = [["8","3",".",".","7",".",".",".","."],
          ["6",".",".","1","9","5",".",".","."],
          [".","9","8",".",".",".",".","6","."],
          ["8",".",".",".","6",".",".",".","3"],
          ["4",".",".","8",".","3",".",".","1"],
          ["7",".",".",".","2",".",".",".","6"],
          [".","6",".",".",".",".","2","8","."],
          [".",".",".","4","1","9",".",".","5"],
          [".",".",".",".","8",".",".","7","9"]]
result2 = solution.isValidSudoku(board2)
print(result2)

# Time Complexity: O(1) - The solution always iterates over a 9x9 Sudoku board, which is a constant size.
# Space Complexity: O(1) - The solution uses sets of constant size to store the seen numbers in each row, column, and sub-box.
# Overall, the space complexity is constant.