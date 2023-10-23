import csv
from SolveSudoku import Solution
# from SolveSudokuBT import BackTrack

answer = [['5', '4', '9', '6', '3', '2', '8', '1', '7'],
          ['1', '2', '3', '9', '8', '7', '5', '4', '6'],
          ['8', '7', '6', '4', '5', '1', '9', '3', '2'],
          ['9', '3', '7', '2', '4', '5', '6', '8', '1'],
          ['2', '5', '1', '8', '9', '6', '4', '7', '3'],
          ['4', '6', '8', '1', '7', '3', '2', '5', '9'],
          ['7', '1', '4', '5', '6', '9', '3', '2', '8'],
          ['6', '8', '2', '3', '1', '4', '7', '9', '5']
          ]
after_elim = [['5', {'9', '4'}, {'9', '4', '6'}, {'9', '6'}, '3', '2', '8', '1', '7'],
              [{'1', '3', '6'}, '2', {'9', '4', '3', '6'}, {'9', '6'}, '8', '7', '5', {'4', '3', '6'}, {'4', '6'}],
              ['8', '7', {'3', '6'}, '4', '5', '1', '9', {'3', '6'}, '2'],
              ['9', '3', '7', '2', '4', '5', {'1', '6'}, '8', {'1', '6'}],
              ['2', '5', '1', '8', '9', '6', '4', '7', '3'],
              ['4', '6', '8', '1', '7', '3', '2', '5', '9'],
              [{'1', '7'}, {'4', '1'}, {'5', '4'}, {'5', '7'}, '6', '9', '3', '2', '8'],
              [{'7', '3', '6'}, '8', '2', {'7', '3'}, '1', '4', {'7', '6'}, '9', '5'],
              [{'1', '7', '3', '6'}, {'9', '4', '1'}, {'5', '9', '4', '3', '6'}, {'5', '7', '3'}, '2', '8', {'1', '7', '6'}, {'4', '6'}, {'6', '4', '1'}]]

board = [['5', '.', '.', '.', '3', '2', '8', '1', '.'],
         ['.', '.', '.', '.', '8', '7', '.', '.', '.'],
         ['8', '7', '.', '4', '5', '.', '9', '.', '2'],
         ['9', '.', '.', '2', '4', '5', '.', '.', '.'],
         ['.', '5', '.', '.', '9', '.', '4', '7', '3'],
         ['4', '.', '8', '1', '.', '.', '2', '.', '9'],
         ['.', '.', '.', '.', '6', '.', '3', '2', '8'],
         ['.', '8', '2', '.', '1', '.', '.', '9', '5'],
         ['.', '.', '.', '.', '.', '8', '.', '.', '.']] 



sln = Solution()
print(sln.solveSudoku(board))

# sln.printboard(ans)


def getBoard():
    with open('100puzzles.csv', 'r') as csvfile:
        spamreader = csv.reader(csvfile)
        

        for row in spamreader:
            puzz = row[0][:82]
            sol = row[0][82:]
            puzz_board = createBoard(puzz)
            myAnswer, isValid = sln.func(puzz_board)
            sol_board = createBoard(sol)
            
            if myAnswer != sol_board and not isValid:
                sln.printboard(createBoard(puzz))
                print("---")
                sln.printboard(createBoard(sol))
                print()
                # sln.printboard(myAnswer)

                print()
                print()
                
                
            # break

def createBoard(nums):
    board = []
    i = 0
    j = i + 9
    while j < len(nums):
        board.append([i if i != '0' else '.' for i in nums[i:j] ])
        i = j
        j += 9
    return board

def reduceBoard(board):
    st = ""
    for i in board:
        for j in i:
            st+=j
    return st

# getBoard()

# def getCandidates(self, board):
#         for row in range(9):
#             for col in range(9):
#                 if type(board[row][col]) == set and len(board[row][col]) > 0:
#                     return board[row][col], row, col
#         return None, -1,-1