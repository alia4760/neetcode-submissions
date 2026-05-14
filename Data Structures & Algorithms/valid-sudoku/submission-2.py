class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = []
        column =[]
        sub_box = [[] for _ in range(9)]
        for i in range(9):
            one_column = []
            one_row = []
            for j in range(9):
                box_row = i//3 * 3
                box_column = j//3
                if board[i][j] != ".":
                    one_row.append(board[i][j])
                    sub_box[box_row + box_column].append(board[i][j])
                if board[j][i] != ".":
                    one_column.append(board[j][i])
            column.append(one_column)
            row.append(one_row)

        for i in range(9):
            one_row = row[i]
            one_column = column[i]
            if len(one_row) != len(set(one_row)):
                print("row")
                return False 
            if len(one_column) != len(set(one_column)):
                print(one_column)
                print("col")
                return False 
            if len(sub_box[i]) != len(set(sub_box[i])):
                print("box")
                return False 
        
        return True 
        
        

        
            
        