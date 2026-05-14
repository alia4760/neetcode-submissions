class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = []
        column =[]
        sub_box = [[] for _ in range(9)]

        for i in range(9):
            one_row = []
            one_column = []
            one_box = []

            for j in range(9):
                # row
                if board[i][j] != ".":
                    one_row.append(board[i][j])
                # column
                if board[j][i] != ".":
                    one_column.append(board[j][i])
                # box
                box_row = (i // 3) * 3 + (j // 3)
                box_col = (i % 3) * 3 + (j % 3)
                if board[box_row][box_col] != ".":
                    one_box.append(board[box_row][box_col])

            if len(one_row) != len(set(one_row)):
                return False
            if len(one_column) != len(set(one_column)):
                return False
            if len(one_box) != len(set(one_box)):
                return False

        return True