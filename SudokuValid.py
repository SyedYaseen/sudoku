# Input:
board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
                                                                                                                                                                                                      ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
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


# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.

class Solution(object):
    def func(self, board):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """


        # sub = {0: {}, 1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}, 7: {}, 8: {}}
        # low_limits = 0
        # high_limit = 2

        memo_row = {}
        memo_col = {}
        for row in range(9):
            for col in range(9):
                # Eliminate by rows
                if board[row][col] != '.':
                    if board[row][col] in memo_row:
                        return False
                    else:
                        memo_row[board[row][col]] = 1

                # Eliminate by colums
                if board[col][row] != '.':
                    if board[col][row] in memo_col:
                        return False
                    else:
                        memo_col[board[col][row]] = 1

            memo_row = {}
            memo_col = {}

        memo_sub = {}
        for grid_x in range(0, 9, 3):
            for grid_y in range(0, 9, 3):
                for row in range(grid_x, grid_x + 3, 1):
                    for col in range(grid_y, grid_y+3, 1):
                        if board[row][col] != '.':
                            if board[row][col] in memo_sub:
                                return False
                            else:
                                memo_sub[board[row][col]] = 1
                memo_sub = {}

        return True


sln = Solution()
print(sln.func(board))
