class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]

        rows = self.generate(numRows - 1)
        last_row = rows[-1]
        new_row = [1]

        for i in range(1, numRows - 1):
            new_row.append(last_row[i - 1] + last_row[i])

        new_row.append(1)
        rows.append(new_row)

        return rows
