class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        minMatrix = []
        for rowIndex, cols in enumerate(matrix):
            if (rowIndex == 0):
                minMatrix.append(cols)
                continue
            minRow = []
            for colIndex, cell in enumerate(cols):
                prevRowIndex = rowIndex - 1
                minRow.append(
                    min(
                        matrix[prevRowIndex][colIndex - 1] if colIndex > 0 else float('inf'),
                        matrix[prevRowIndex][colIndex],
                        matrix[prevRowIndex][colIndex + 1] if colIndex + 1 < len(cols) else float('inf')
                        )
                    + cell
                    )
            minMatrix.append(minRow)
        return min(minMatrix[-1])
