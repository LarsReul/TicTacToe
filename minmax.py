import fieldClass

def minimax(field: fieldClass.Field, depth: int):
    if (depth % 2 == 1) and field.winningPlayer() is not None and field.winningPlayer() != field.currentPlayer():
        return {"score": 10}
    elif (depth % 2 == 0) and field.winningPlayer() is not None and field.winningPlayer() != field.currentPlayer():
        return {"score": -10}
    if not field.getEmptyPositions():
        return {"score": 0}

    moves = []
    for position in field.getEmptyPositions():
        move = {"position": position}
        field.setTic(position)
        result = minimax(field, depth + 1)
        move["score"] = result["score"]

        field.clearTic(position)
        moves.append(move)


    if depth % 2 == 0:
        bestMove = (0, 0)
        bestScore = -10000
        for move in moves:
            if move["score"] > bestScore:
                bestScore = move["score"]
                bestMove = move
    else:
        bestMove = (0, 0)
        bestScore = 10000
        for move in moves:
            if move["score"] < bestScore:
                bestScore = move["score"]
                bestMove = move

    return bestMove

