from SolveSudoku import SolveSudoku
import copy
soln = SolveSudoku()

class BackTrack(object):
    modifiableBoard = None

    def getCandidates(self, board):
        for row in range(9):
            for col in range(9):
                if type(board[row][col]) == set and len(board[row][col]) > 0:
                    return board[row][col], row, col
        return None, -1,-1
    
    def isValid(self, row, col):
        memo_row = set()
        memo_col = set()
        
        for i in range(0,9):
            if type(self.modifiableBoard[i][col]) != set:
                if self.modifiableBoard[i][col] in memo_row:
                    return False
                else:
                    memo_row.add(self.modifiableBoard[i][col])

            if type(self.modifiableBoard[row][i]) != set:
                if self.modifiableBoard[row][i] in memo_col:
                    return False
                else:
                    memo_col.add(self.modifiableBoard[row][i])
            


        memo_sqr = set()
        x = (row // 3) * 3
        y = (col // 3) * 3

        for i in range(x, x+3, 1):
            for j in range(y, y+3, 1):
                if type(self.modifiableBoard[i][j]) != set:
                    if self.modifiableBoard[i][j] in memo_sqr:
                        return False
                    else:
                        memo_sqr.add(self.modifiableBoard[i][j])

        return True


    def Solve(self, board):
        FinalEmpties, isValid, board = soln.eliminationByRowColumnSquare(board, 0)

        if isValid:
            self.modifiableBoard = copy.deepcopy(board)
            self.solveRecursively(id, 0)
            
    
    def solveRecursively(self, id):
        if id == 81:
            return True
        
        row = id // 9
        col = id % 9

        for candidate in range(1,10,1):
            if type(self.modifiableBoard[row][col]) == set:
                self.board[row][col] = str(candidate)
                if self.isValid(row, col) and self.solveRecursively(id+1):
                    return True
            else:
                return self.solveRecursively(id+1)
            