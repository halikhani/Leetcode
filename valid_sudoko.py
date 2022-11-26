# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
 

# Example 1:


# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
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

# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

# Constraints:

# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        import numpy as np
        int_board = []
        
        for i in range(len(board)):
            row = [0]*len(board[i])
            for j in range(len(board[i])):
                row[j] = -1 if board[i][j] == '.' else int(board[i][j])
            
            int_board.append(row)
        int_board = np.array(int_board)
        
        # checking rows:
        for i in range(len(int_board)):
            tmp_dict = dict()
            for j in range(len(int_board[i])):
                if int_board[i][j] == -1:
                    continue
                elif int_board[i][j] in tmp_dict.keys():
                    return False
                else:
                    tmp_dict[int_board[i][j]] = int_board[i][j]
        
        #checking cols
        for i in range(len(int_board)):
            col_list = int_board[:, i]
            tmp_dict = dict()
            for c in col_list:
                if c == -1:
                    continue
                elif c in tmp_dict.keys():
                    return False
                else:
                    tmp_dict[c] = c
        
        # checking blocks
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                block = int_board[i:i+3, j:j+3]
                block = block.flatten()
                tmp_dict = dict()
                for c in block:
                    if c == -1:
                        continue
                    elif c in tmp_dict.keys():
                        return False
                    else:
                        tmp_dict[c] = c
                        
        return True