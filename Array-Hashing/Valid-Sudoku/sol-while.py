from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]])-> bool:
        boxes = [set() for _ in range(9)]
        i = 0
        while i < len(board):
            row_set = set()
            j = 0
            while j < len(board[i]):
                cell = board[i][j]
                if cell != ".":
                    box_idx = (i // 3) * 3 + (j // 3)
                    if cell in row_set or cell in boxes[box_idx]:
                        return False
                    else:
                        row_set.add(cell)
                        boxes[box_idx].add(cell)
                j += 1
            i += 1
    
        j = 0
        while j<len(board):
            col_set = set()
            i = 0
            while i< len(board[j]):
                cell = board[i][j]
                if cell != ".":
                    if cell not in col_set:
                        col_set.add(cell)
                    else:
                        return False
                i+=1
            j+=1    
        return True
    
            
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
    
