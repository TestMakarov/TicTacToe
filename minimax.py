def wins(grid):
    rows = [[grid[i+j] for j in (0, 1, 2)] for i in (0, 3, 6)]
    cols = [[grid[i+j] for j in (0, 3, 6)] for i in (0, 1, 2)]
    digs = [[grid[i] for i in (0, 4, 8)], [grid[i] for i in (2, 4, 6)]]
    return any(all(cell is 'x' for cell in row) or
               all(cell is 'o' for cell in row)
               for row in rows + cols + digs)

def full(grid):
    return all(cell is 'x' or cell is 'o' for cell in grid)

def move(grid, cell, symbol):
    moved = list(grid)
    moved[cell] = symbol
    return moved

def moves(grid, symbol):
    return [move(grid, cell, symbol) for cell in (0, 1, 2, 3, 4, 5, 6, 7, 8)
            if grid[cell] not in ('x', 'o')]

def minimax(grid, symbol):
    if wins(grid):
        return (1 if symbol is 'o' else -1), None
    elif full(grid):
        return 0, None
    elif symbol is 'x':
        best_score = -2
        best_move = None
        for move in moves(grid, 'x'):
            score, mv = minimax(move, 'o')
            if score >= best_score:
                best_score = score
                best_move = move
        return best_score, best_move
    elif symbol is 'o':
        best_score = 2
        best_move = None
        for move in moves(grid, 'o'):
            score, mv = minimax(move, 'x')
            if score <= best_score:
                best_score = score
                best_move = move
        return best_score, best_move

def tictac(grid, turn):
    score, move = minimax(grid, turn)
    return grid, ''.join(move)
def get(grid):
    return tictac(grid, "o")[1]

