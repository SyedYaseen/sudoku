modifiableBoard =[['5', '1', '1', '1', '3', '2', '8', '1', '1'], ['1', '1', '1', '1', '8', '7', '1', '1', '1'], ['8', '7', '1', '4', '5', '1', '9', '1', '2'], ['9', '1', '1', '2', '4', '5', '1', '1', '1'], ['1', '5', '1', '1', '9', '6', '4', '7', '3'], ['4', '1', '8', '1', '7', '1', '2', '1', '9'], ['1', '1', '1', '1', '6', '1', '3', '2', '8'], ['1', '8', '2', '1', '1', '1', '1', '9', '5'], ['1', '1', '1', '1', '1', '8', '1', '1', '1']]

def checkValid( row, col):
    memo_row = set()
    memo_col = set()
    
    for i in range(0,9):
        if type(modifiableBoard[i][col]) != set:
            if modifiableBoard[i][col] in memo_row:
                return False
            else:
                memo_row.add(modifiableBoard[i][col])

        if type(modifiableBoard[row][i]) != set:
            if modifiableBoard[row][i] in memo_col:
                return False
            else:
                memo_col.add(modifiableBoard[row][i])
        
    memo_sqr = set()
    x = (row // 3) * 3
    y = (col // 3) * 3

    for i in range(x, x+3, 1):
        for j in range(y, y+3, 1):
            if type(modifiableBoard[i][j]) != set:
                if modifiableBoard[i][j] in memo_sqr:
                    return False
                else:
                    memo_sqr.add(modifiableBoard[i][j])

    return True

print(checkValid(8,8))