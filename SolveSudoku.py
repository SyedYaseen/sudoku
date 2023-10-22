import copy
# # Input:
# needs 10 loops of elimination script (only) to complete
# board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
#          ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#          [".", "9", "8", ".", ".", ".", ".", "6", "."],
#          ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#          ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#          ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#          [".", "6", ".", ".", ".", ".", "2", "8", "."],
#          [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

# correctAns = [["5", "3", "4", "6", "7", "8", "9", "1", "2"],
#               ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
#               ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
#               ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
#               ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
#               ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
#               ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
#               ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
#               ["3", "4", "5", "2", "8", "6", "1", "7", "9"]]


board = [[".", ".", "9", "7", "4", "8", ".", ".", "."],
         ["7", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", "2", ".", "1", ".", "9", ".", ".", "."],
         [".", ".", "7", ".", ".", ".", "2", "4", "."],
         [".", "6", "4", ".", "1", ".", "5", "9", "."],
         [".", "9", "8", ".", ".", ".", "3", ".", "."],
         [".", ".", ".", "8", ".", "3", ".", "2", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "6"],
         [".", ".", ".", "2", "7", "5", "9", ".", "."]]


# board = [['.', '.', '9', '.', '.', '1', '.', '5', '2'],
#          ['.', '.', '3', '.', '.', '.', '.', '1', '4'],
#          ['.', '.', '1', '5', '.', '.', '.', '6', '8'],
#          ['1', '7', '2', '4', '3', '5', '8', '9', '6'],
#          ['3', '6', '5', '8', '9', '2', '1', '4', '7'],
#          ['8', '9', '4', '1', '6', '7', '2', '3', '5'],
#          ['.', '1', '7', '.', '.', '8', '6', '2', '.'],
#          ['9', '.', '8', '.', '.', '.', '5', '7', '.'],
#          ['2', '.', '6', '7', '.', '.', '4', '8', '.']]

# board = [[".", ".", ".", ".", ".", "1", ".", ".", "2"],
#          [".", ".", "3", ".", ".", ".", ".", ".", "4"],
#          [".", ".", ".", "5", ".", ".", ".", "6", "."],
#          [".", "7", ".", ".", "3", ".", "8", ".", "."],
#          ["3", ".", "5", ".", "9", ".", "1", ".", "7"],
#          [".", ".", "4", ".", "6", ".", ".", "3", "."],
#          [".", "1", ".", ".", ".", "8", ".", ".", "."],
#          ["9", ".", ".", ".", ".", ".", "5", ".", "."],
#          ["2", ".", ".", "7", ".", ".", ".", ".", "."]]

# Answer
# ['6', '4', '9', '3', '8', '1', '7', '5', '2']
# ['5', '8', '3', '2', '7', '6', '9', '1', '4']
# ['7', '2', '1', '5', '4', '9', '3', '6', '8']
# ['1', '7', '2', '4', '3', '5', '8', '9', '6']
# ['3', '6', '5', '8', '9', '2', '1', '4', '7']
# ['8', '9', '4', '1', '6', '7', '2', '3', '5']
# ['4', '1', '7', '9', '5', '8', '6', '2', '3']
# ['9', '3', '8', '6', '2', '4', '5', '7', '1']
# ['2', '5', '6', '7', '1', '3', '4', '8', '9']


class SolveSudoku(object):
    '''Finds triples on the emptyVal dict group by row, column or square
    and returns a list of triples on that group'''

    row_group = None
    col_group = None
    sqr_group = None

    triplesRow = None
    triplesCol = None
    triplesSquare = None

    possible = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
    # possible = {1,2,3,4,5,6,7,8,9}

    def getSquare(self, rowInt, colInt):
        if 0 <= rowInt <= 2 and 0 <= colInt <= 2:
            return 0
        elif 0 <= rowInt <= 2 and 3 <= colInt <= 5:
            return 1
        elif 0 <= rowInt <= 2 and 6 <= colInt <= 8:
            return 2
        elif 3 <= rowInt <= 5 and 0 <= colInt <= 2:
            return 3
        elif 3 <= rowInt <= 5 and 3 <= colInt <= 5:
            return 4
        elif 3 <= rowInt <= 5 and 6 <= colInt <= 8:
            return 5
        elif 6 <= rowInt <= 8 and 0 <= colInt <= 2:
            return 6
        elif 6 <= rowInt <= 8 and 3 <= colInt <= 5:
            return 7
        elif 6 <= rowInt <= 8 and 6 <= colInt <= 8:
            return 8

    def getSquareLimits(self, squareNo):
        rowMin = rowMax = colMin = colMax = None
        if squareNo in [0, 1, 2]:
            rowMin = 0
            rowMax = 3
        elif squareNo in [3, 4, 5]:
            rowMin = 3
            rowMax = 6
        elif squareNo in [6, 7, 8]:
            rowMin = 6
            rowMax = 9

        if squareNo in [0, 3, 6]:
            colMin = 0
            colMax = 3
        elif squareNo in [1, 4, 7]:
            colMin = 3
            colMax = 6
        elif squareNo in [2, 5, 8]:
            colMin = 6
            colMax = 9
        return rowMin, rowMax, colMin, colMax

    def mapTriples(self, index, group, map):
        if len(map[index]) == 0:
            triples = self.findTriples(group)
            if len(triples) > 0:
                map[index] = triples

    def findTriples(self, lis_group):
        only_three = []
        only_two = []
        triples = []

        for i in lis_group:
            if len(i) == 3:
                only_three.append(i)
            if len(i) == 2:
                only_two.append(i)
        # print("only three", only_three)
        # print("only two", only_two)
        temp = []
        for i in only_three:
            if i in temp:
                temp.append(i)
            else:
                temp = [i]

            for two in only_two:
                if two.issubset(i):
                    temp.append(two)
            if len(temp) >= 3:
                triples.append(temp[0])
        return triples

    def eliminationByRowColumnSquare(self, board, FinalEmpties):
        square_values = [set() for _ in range(9)]
        row_values = [set() for _ in range(9)]
        col_values = [set() for _ in range(9)]
        self.row_group = [[] for _ in range(9)]
        self.col_group = [[] for _ in range(9)]
        self.sqr_group = [[] for _ in range(9)]

        isValid = True

        for row in range(9):
            for col in range(9):
                if type(board[row][col]) == set and len(board[row][col]) == 0:
                    print("Invalid - Empty set", row, col)
                    isValid = False
                    self.printboard(board)
                    return -1, isValid, board

                if type(board[row][col]) == str and board[row][col] != '.':
                    sqrNo = self.getSquare(row, col)

                    row_values[row].add(board[row][col])
                    square_values[sqrNo].add(
                        board[row][col])

                if type(board[col][row]) == str and board[col][row] != '.':
                    sqrNo = self.getSquare(col, row)

                    col_values[row].add(board[col][row])
                    square_values[sqrNo].add(
                        board[col][row])

        for row in range(9):
            for col in range(9):
                if board[row][col] == '.' or type(board[row][col]) == set:
                    squareNo = self.getSquare(row, col)
                    candidates = self.possible - \
                        row_values[row] - col_values[col] - \
                        square_values[squareNo]

                    FinalEmpties += 1

                    if not bool(candidates):
                        isValid = False
                        return -1, isValid, board

                    if len(candidates) == 1:
                        FinalEmpties -= 1
                        board[row][col] = candidates.pop()
                    else:
                        board[row][col] = candidates
                        self.row_group[row].append(candidates)
                        self.col_group[col].append(candidates)
                        self.sqr_group[squareNo].append(candidates)
        return FinalEmpties, isValid, board

    def EliminateByTriples(self, board):
        for row in range(9):
            for col in range(9):
                self.mapTriples(row, self.row_group[row], self.triplesRow)
                self.mapTriples(col, self.col_group[col], self.triplesCol)

                squareNo = self.getSquare(row, col)
                self.mapTriples(
                    squareNo, self.sqr_group[squareNo], self.triplesSquare)

                squareNo = self.getSquare(col, row)
                self.mapTriples(
                    squareNo, self.sqr_group[squareNo], self.triplesSquare)

        for i in range(9):
            if len(self.triplesRow[i]) != 0 and len(self.row_group[i]) > 3:
                for tri in self.triplesRow[i]:
                    for col in range(9):
                        if type(board[i][col]) == set and not set(board[i][col]).issubset(tri):
                            newCandidates = board[i][col] - tri
                            if newCandidates != board[i][col] and board[i][col] in self.row_group[i]:
                                self.row_group[i].remove(board[i][col])
                                self.row_group[i].append(newCandidates)
                                board[i][col] = newCandidates

            if len(self.triplesCol[i]) != 0 and len(self.col_group[i]) > 3:
                for tri in self.triplesCol[i]:
                    for row in range(9):
                        if type(board[row][i]) == set and not set(board[row][i]).issubset(tri):
                            newCandidates = board[row][i] - tri
                            if newCandidates != board[row][i] and board[row][i] in self.col_group[i]:
                                self.col_group[i].remove(board[row][i])
                                self.col_group[i].append(newCandidates)
                                board[row][i] = newCandidates

            if len(self.triplesSquare[i]) != 0 and len(self.sqr_group[i]) > 3:
                for tri in self.triplesSquare[i]:
                    rowMin, rowMax, colMin, colMax = self.getSquareLimits(i)
                    for row in range(rowMin, rowMax):
                        for col in range(colMin, colMax):
                            if type(board[row][col]) == set and not board[row][col].issubset(tri):
                                newCandidates = board[row][col] - tri
                                if newCandidates != board[row][col] and board[row][col] in self.sqr_group[i]:
                                    self.sqr_group[i].remove(
                                        board[row][col])
                                    self.sqr_group[i].append(newCandidates)
                                    board[row][col] = newCandidates

    def AssignToBoard(self, board):
        for row in range(9):
            for col in range(9):
                if type(board[row][col]) == set and len(board[row][col]) == 0:
                    return None
                if type(board[row][col]) == set and len(board[row][col]) == 1:
                    board[row][col] = board[row][col].pop()

    def runElimination(self, board):
        timesRun = 0
        InitEmpties = 99
        FinalEmpties = 0
        isValid = True

        while FinalEmpties != InitEmpties and isValid:
            timesRun += 1
            # Reset row groups each time
            self.row_group = [[] for _ in range(9)]
            self.col_group = [[] for _ in range(9)]
            self.sqr_group = [[] for _ in range(9)]

            self.triplesRow = [[] for _ in range(9)]
            self.triplesCol = [[] for _ in range(9)]
            self.triplesSquare = [[] for _ in range(9)]

            FinalEmpties, isValid, board = self.eliminationByRowColumnSquare(
                board, FinalEmpties)

            if not isValid:
                print("isvalid")
                return board, False, FinalEmpties

            self.EliminateByTriples(board)
            self.AssignToBoard(board)

            if FinalEmpties < InitEmpties:
                InitEmpties = FinalEmpties
                FinalEmpties = 0
        # print("TimesRun", timesRun, "Empties", FinalEmpties)

        return board, isValid, FinalEmpties

    def boardIsValid(self, board):
        for row in range(9):
            unique = set()
            for col in range(9):
                if board[row][col] == '.':
                    self.proceed = True
                    return
                elif type(board[row][col]) != set:
                    if board[row][col] not in unique:
                        unique.add(board[row][col])
                    else:
                        self.invalid == True

        self.proceed = True
        # return True

    def printboard(self, board):
        for i in board:
            # print()
            print(i)

    def getCandidates(self, board):
        r = c = -1
        candidates = None
        empties = 0
        for row in range(9):
            row_unique = set()
            col_unique = set()
            for col in range(9):
                rowitem = board[row][col]
                colitem = board[col][row]

                if type(rowitem) == set:
                    if len(rowitem) == 0:
                        return (False, r, c, None)
                    else:
                        empties += 1
                        if candidates is None:
                            candidates = rowitem
                            r = row
                            c = col

                if type(colitem) == set and len(colitem) == 0:
                    return (False, r, c, None)

                if type(rowitem) == str:
                    if rowitem in row_unique:
                        return (False, r, c, None)
                    else:
                        row_unique.add(rowitem)

                if type(colitem) == str:
                    if colitem in col_unique:
                        return (False, r, c, None)
                    else:
                        col_unique.add(colitem)

        if empties == 0 and candidates == None:
            return (True, r, c, None)

        return (False, r, c, candidates)

    def loopThrough(self, board, isComplete=False):
        if board is None:
            return False,  None

        isComplete, row, col, candidates = self.getCandidates(board)
        if isComplete:
            return True, board
        if row == -1:
            # print("Here")
            return False, board

        while bool(candidates) and not isComplete:
            tempBoard = board.copy()
            tempBoard[row][col] = candidates.pop()
            print("Picked for board", row, col, tempBoard[row][col])
            eliminatedBoard = self.runElimination(tempBoard)

            board, isComplete = self.loopThrough(eliminatedBoard)
            if board == None:
                break

    def func(self, board):
        isComplete = False
        board, isValid, FinalEmpties = self.runElimination(board)
        print("Before candi picking")
        self.printboard(board)
        print()

        if not isValid:
            return board, isValid

        if isValid and FinalEmpties != 0:
            isComplete, row, col, candidates = self.getCandidates(board)

            if not isComplete and row != -1:
                while bool(candidates) and isComplete == False:
                    tempBoard = copy.deepcopy(board)
                    tempBoard[row][col] = candidates.pop()
                    tempBoard, isValid, FinalEmpties = self.runElimination(
                        tempBoard)
                    if isValid and FinalEmpties == 0:
                        board = tempBoard
                        break
                    if not isValid:
                        board = tempBoard
        return board, isValid



