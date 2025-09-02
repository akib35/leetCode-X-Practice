import math

def mrvVariableSelection(variables:list[str], domains:dict)->str:
    min_var = ""
    min_domain_size = math.inf

    for var in variables:
        domain_size = len(domains[var])
        if domain_size < min_domain_size:
            min_domain_size = domain_size
            min_var = var

    return min_var

def fewestCandidates(board: list[list[str]])->tuple:
    rows, cols = len(board), len(board[0])
    min_operations = math.inf
    best_cell = (-1, -1)
    candidates = []

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == '.':
                used = set()

                for k in range(9):
                    if board[k][j] != '.':
                        used.add(board[k][j])
                    if board[i][k] != '.':
                        used.add(board[i][k])

                    box_row, box_col = 3 * (i // 3), 3 * (j // 3)
                    if board[box_row + k // 3][box_col + k % 3] != '.':
                        used.add(board[box_row + k // 3][box_col + k % 3])
                    if len(used) == 9:
                        break
                cell_candidates = [str(num) for num in range(1, 10) if str(num) not in used]
                if len(cell_candidates) < min_operations:
                    min_operations = len(cell_candidates)
                    best_cell = (i, j)
                    candidates.append((i, j, cell_candidates))

    return best_cell, candidates
