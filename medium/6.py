# 2023.05.09

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [''] * numRows
        i = 0
        increase = True

        for char in s:
            rows[i] += char

            if i == numRows - 1:
                increase = False
            elif i == 0:
                increase = True

            i += 1 if increase else -1

        return ''.join(rows)
        