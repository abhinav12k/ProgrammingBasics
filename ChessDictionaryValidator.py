def isValidPosition(pos):
    print(pos)
    return int(pos[0]) >= 1 and int(pos[0]) <= 8 and pos[1] >= 'a' and pos[1] <= 'h' 

def isValidChessBoard(chessboard):
    
    whitePieces = {}
    maxWhitePieces = 0
    blackPieces = {}
    maxBlackPieces = 0

    for key, value in chessboard.items():
        if not isValidPosition(key):
            return False

        if value[0] != 'b' or value[0] != 'w':
            return False
        
        if value[0] == 'w':
            whitePieces.setdefault(value[1:],0)
            whitePieces[value[1:]] = whitePieces[value[1:]] + 1
        else:
            blackPieces.setdefault(value[1:],0)
            blackPieces[value[1:]] = blackPieces[value[1:]] + 1
    
    whitePawns = whitePieces.get("pawn",0)
    if whitePawns > 8:
        return False
    
    blackPawns = blackPieces.get("pawn",0)
    if blackPawns > 8:
        return False

    maxWhitePieces = maxWhitePieces + whitePawns + whitePieces.get("knight",0) + whitePieces.get("bishop",0) + whitePieces.get("rook",0) + whitePieces.get("queen",0) + whitePieces.get("king",0)
    if maxWhitePieces > 16:
        return False
    
    maxBlackPieces = maxBlackPieces+ blackPawns + blackPawns.get("knight",0) + blackPawns.get("bishop",0) + blackPawns.get("rook",0) + blackPawns.get("queen",0) + blackPawns.get("king",0)
    if maxBlackPieces > 16:
        return False


chessBoard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

print(isValidChessBoard(chessBoard))