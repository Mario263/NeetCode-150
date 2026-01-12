from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]])-> bool:
        row = set()
        col = set()
        square = set()
        i = 0
        # while i < len(board):
        #     j=0
        for i in range(len(board)):
            row_set = set()
        for j in range(len(board[i])):
            if board[i][j] != ".":
                if board[i][j] in row_set:
                    print(f"Duplicate {board[i][j]} found in row {i}")
                else:
                    row_set.add(board[i][j])
        print(f"Row {i} contents:", row_set)
            
        #     while j < len(board[i]):   
        #         if board[i][j] == ".":
        #             j+=1
        #         elif board[i][j] not in row:
        #             row.add(board[i][j])
        #         j+=1
        #         if j > len(board[i]):
        #             break
        #     i+=1
        # print(f"Row {i} contents:", row)
        # j = 0c
        # while j < len(board):
        #     i=0
        #     while i< len(board[j]):
        #         if board[j][i] == ".":
        #             i+=1
        #         elif board[j][i] not in col:
        #             col.add(board[j][i])
        #         i+=1
        #     j+=1
        # print(f"Column {j} contents:", col)
        # return row, col

        # return square.add(row,col)
    
    
if __name__ == "__main__":
    print(Solution().isValidSudoku([
        ["1","2",".",".","3",".",".",".","."],
        ["1",".","2","5",".","4",".",".","."],
        [".","9","1",".",".",".",".",".","3"],
        ["5",".",".",".","6",".",".",".","4"],
        [".",".",".","8",".","3",".",".","5"],
        ["7",".",".",".","2",".",".",".","6"],
        [".",".",".",".",".",".","2",".","."],
        [".",".",".","4","1","9",".",".","8"],
        [".",".",".",".","8",".",".","7","9"]]))