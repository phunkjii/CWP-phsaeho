def checkmate(board):
    Board2D = setBoard(board)

    if not Board2D:
        print("Error")
        return

    n = len(Board2D)
    for row in Board2D:
        if len(row) != n:
            print("Error")
            return
    
    king = findKing(Board2D)
    if king is None:
        print("Error")
        return

    for i in range(n):
        for j in range(n):
            piece = Board2D[i][j]

            if piece == "P" and Pawn(Board2D, i, j, king):
                print("Success")
                return

            if piece == "B" and Bishop(Board2D, i, j, king):
                print("Success")
                return

            if piece == "R" and Rook(Board2D, i, j, king):
                print("Success")
                return

            if piece == "Q" and Queen(Board2D, i, j, king):
                print("Success")
                return          

    # 4. ถ้าไม่มีหมากตัวไหนรุก King ได้ ให้แสดง Fail
    print("Fail")
    

def setBoard(board):
    if not isinstance(board, str) or not board.strip():
        return []
        
    rowsList = []
    for row in board.split("\n"):
        cleanRow = row.strip()
        if cleanRow:
            rowsList.append(cleanRow)

    Board2D = []
    for r in rowsList:
        Board2D.append(list(r))

    return Board2D


def findKing(board):
    king = None
    n = len(board)
    for i in range(n):
        for j in range(len(board[i])):
            if board[i][j] == "K":
                if king is not None: 
                    # มี King มากกว่า 1 ตัว
                    return None
                king = (i, j)
    return king


def Pawn(Board2D, i, j, king):
    kingRow, kingCol = king 
    attacks = [(i - 1, j - 1), (i - 1, j + 1)]
    return (kingRow, kingCol) in attacks


def Bishop(Board2D, i, j, king):
    n = len(Board2D)
    kingRow, kingCol = king
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

    for iChange, jChange in directions:
        x = i + iChange
        y = j + jChange
        while 0 <= x < n and 0 <= y < n:
            if (x, y) == (kingRow, kingCol):
                return True
            if Board2D[x][y] != ".":
                break
            x += iChange
            y += jChange
    return False


def Rook(Board2D, i, j, king):
    n = len(Board2D)
    kingRow, kingCol = king
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for iChange, jChange in directions:
        x = i + iChange
        y = j + jChange
        while 0 <= x < n and 0 <= y < n:
            if (x, y) == (kingRow, kingCol):
                return True
            if Board2D[x][y] != ".":
                break
            x += iChange
            y += jChange
    return False


def Queen(Board2D, i, j, king):
    return Rook(Board2D, i, j, king) or Bishop(Board2D, i, j, king)
