def PowTwo(n:int)->bool:
    return n & (n-1) == 0 and n!=0

def countSetBits(n:int)->int:
    count = 0
    while n:
        n &= (n-1)
        count+=1
    return count

def generateSubsets(nums:list)->list:
    length = len(nums)
    subsets = []
    for mask in range(1<<length):
        subset = []
        for i in range(length):
            if mask & (1<<i):
                subset.append(nums[i])
        subsets.append(subset)
    return subsets


import math

def maxSum( nums:list ) -> int:
    max_sum = 0

    def last_digit(n:int)->int:
        return n&1

    def bin_length(n:int)->int:
        if n==0:
            return 1
        else: return math.floor(math.log2(n))+1

    def cal_sum(mask)->None:
        nonlocal max_sum
        if bin_length(mask)>len(nums):
            return
        sum = 0
        for i in range(len(nums)):
            if mask & (1<<i):
                sum+=nums[i]

        max_sum = max(max_sum, sum)
        if last_digit(mask)==0:
            cal_sum(mask*2)
            cal_sum(mask*2+1)
        else:
            cal_sum(mask*2)

    cal_sum(1)
    return max_sum

def sudokuSolver(board: list[list[str]]) -> None:
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

    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                empty_cells.append((i, j))
            else:
                create_mask(i, j, int(board[i][j]) - 1)

    def solve(index):
        if index == len(empty_cells):
            return True

        row, col = empty_cells[index]
        box_index = (row // 3) * 3 + (col // 3)
        for num in range(9):
            mask = 1 << num
            if (row_mask[row] & mask) == 0 and (col_mask[col] & mask) == 0 and (box_mask[box_index] & mask) == 0:
                board[row][col] = str(num + 1)
                create_mask(row, col, num)

                if solve(index + 1):
                    return True

                board[row][col] = '.'
                remove_mask(row, col, num)

        return False

    solve(0)
