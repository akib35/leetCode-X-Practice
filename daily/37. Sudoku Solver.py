## Backtracking
## Time Complexity: O(9^81)
## Space Complexity: O(1)
class Solution_brute_force:
    def solveSudoku(self, board: list[list[str]]) -> None:
        # validity check
        def isValid(board, row, col, ch):
            for i in range(9):
                if board[row][i] == ch: return False
                if board[i][col] == ch: return False
                if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == ch: return False
            return True

        # backtracking
        def solve(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for ch in "123456789":
                            if isValid(board, i, j, ch):
                                board[i][j] = ch
                                if solve(board): return True
                                board[i][j] = '.'
                        return False
            return True

        solve(board)


class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row_mask = [0] * 9
        col_mask = [0] * 9
        box_mask = [0] * 9
        empty_cells = []

        def create_mask(row, col, pos):
            mask = 1 << pos
            row_mask[row] |= mask
            col_mask[col] |= mask
            box_mask[(row // 3) * 3 + (col // 3)] |= mask

        def remove_mask(row, col, pos):
            mask = ~(1 << pos)
            row_mask[row] &= mask
            col_mask[col] &= mask
            box_mask[(row // 3) * 3 + (col // 3)] &= mask

        def count_set_bits(n):
            count = 0
            while n:
                n &= (n - 1)
                count += 1
            return count

        def bit_position(mask):
            # Returns the position of the least significant set bit (0-based)
            pos = 0
            while (mask & 1) == 0:
                mask >>= 1
                pos += 1
            return pos

        def find_best_cell():
            """Find the empty cell with the fewest candidates using MRV heuristic."""
            min_options = 10
            idx = -1
            candidates_mask = 0

            for k, (row, col) in enumerate(empty_cells):
                used = row_mask[row] | col_mask[col] | box_mask[(row // 3) * 3 + (col // 3)]
                available = (~used) & 0x1FF
                options = count_set_bits(available)
                if options < min_options:
                    min_options = options
                    idx = k
                    candidates_mask = available
                    if min_options == 1:
                        break

            return idx, candidates_mask

        def try_candidates(row, col, candidates_mask):
            """Try all candidates for a given cell."""
            mask = candidates_mask
            while mask:
                pick = mask & (-mask)
                pos = bit_position(pick)
                create_mask(row, col, pos)
                board[row][col] = str(pos + 1)
                if backtrack():
                    return True
                remove_mask(row, col, pos)
                board[row][col] = '.'
                mask &= mask - 1
            return False

        # Initialize masks and empty cells list
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty_cells.append((i, j))
                else:
                    create_mask(i, j, int(board[i][j]) - 1)

        def backtrack():
            if not empty_cells:
                return True

            idx, candidates_mask = find_best_cell()
            row, col = empty_cells.pop(idx)

            success = try_candidates(row, col, candidates_mask)

            if not success:
                empty_cells.insert(idx, (row, col))

            return success

        backtrack()
