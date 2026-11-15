class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Valid needs to be 3 checks
        
        # The first check
        for row in board:
            nums = [num for num in row if num != "."]
            if len(nums) != len(set(nums)):
                return False
        
        # Second check
        for j in range(9):
            column = [row[j] for row in board if row[j] != "."]

            if len(column) != len(set(column)):
                return False

        # Third check
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = []

                for row in range(i, i + 3):
                    for col in range(j, j + 3):
                        if board[row][col] != ".":
                            box.append(board[row][col])

                if len(box) != len(set(box)):
                    return False

        return True