import heapq
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [set() for x in range(9)]
        cols = [set() for x in range(9)]
        squares = [[set() for x in range(3)] for y in range(3)]

        for x in range(9):
            for y in range(9):
                if board[x][y] == ".":
                    continue
                if board[x][y] in rows[x] or board[x][y] in cols[y] or board[x][y] in squares[x//3][y//3]:
                    return False
                
                
                rows[x].add(board[x][y])
                cols[y].add(board[x][y])
                squares[x//3][y//3].add(board[x][y])

        return True
    
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(Solution().isValidSudoku(board))