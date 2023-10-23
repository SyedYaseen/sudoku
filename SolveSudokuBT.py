from SolveSudoku import SolveSudoku
import copy
soln = SolveSudoku()

class BackTrack(object):
    

    def solveSudoku(self, board):
        
        FinalEmpties, isValid, board = soln.eliminationByRowColumnSquare(board, 0)
        modifiableBoard = copy.deepcopy(board)

        def checkValid( row, col):
            memo_row = set()
            memo_col = set()
            
            for i in range(0,9):
                if type(board[i][col]) != set:
                    if board[i][col] in memo_row:
                        return False
                    else:
                        memo_row.add(board[i][col])

                if type(board[row][i]) != set:
                    if board[row][i] in memo_col:
                        return False
                    else:
                        memo_col.add(board[row][i])
                
            memo_sqr = set()
            x = (row // 3) * 3
            y = (col // 3) * 3

            for i in range(x, x+3, 1):
                for j in range(y, y+3, 1):
                    if type(board[i][j]) != set:
                        if board[i][j] in memo_sqr:
                            return False
                        else:
                            memo_sqr.add(board[i][j])

            return True
        
        def solveRecursively(cellId):
            if cellId == 81:
                return True
            
            row = cellId // 9
            col = cellId % 9

            for candidate in range(1,10,1):
                if type(modifiableBoard[row][col]) == set:
                    board[row][col] = str(candidate)
                    if checkValid(row, col) and solveRecursively(cellId+1):
                        return True
                else:
                    return solveRecursively(cellId+1)
            board[row][col] = set()
            return False
        
        if isValid:
            solveRecursively(0)
            return board
        


