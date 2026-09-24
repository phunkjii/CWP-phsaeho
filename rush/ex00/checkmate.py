PIECES = {"P", "B", "R", "Q"}

def checkmate(board):
    Board2D = setBoard(board)

    # 1. ตรวจสอบว่ากระดานมีข้อมูล และเป็นสี่เหลี่ยมจัตุรัสหรือไม่ (N x N)
    if not Board2D:
        print("Error")
        return

    n = len(Board2D)
    for row in Board2D:
        if len(row) != n:
            print("Error")
            return
    
    # 2. ค้นหาตำแหน่ง King
    king = findKing(Board2D)
    if king is None:
        print("Error")
        return

    # 3. วนลูปตรวจหมากทุกตัวบนกระดานว่ามีตัวไหนรุก King ได้หรือไม่
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
    if not isinstance(board, str) or not board:
        return []

    lines = board.split("\n")
    # ลบบรรทัดว่างหัว-ท้าย
    if lines and lines[0] == "":
        lines.pop(0)
    if lines and lines[-1] == "":
        lines.pop()

    if not lines:
        return []

    # ลบ \r ท้ายบรรทัด (ถ้ามาจากระบบ Windows)
    lines = [line.rstrip("\r") for line in lines]
    return [list(row) for row in lines]


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
            if Board2D[x][y] in PIECES:  # เฉพาะตัวหมากศัตรูเท่านั้นที่เป็นสิ่งกีดขวาง
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
            if Board2D[x][y] in PIECES:  # เฉพาะตัวหมากศัตรูเท่านั้นที่เป็นสิ่งกีดขวาง
                break
            x += iChange
            y += jChange
    return False


def Queen(Board2D, i, j, king):
    return Rook(Board2D, i, j, king) or Bishop(Board2D, i, j, king)
