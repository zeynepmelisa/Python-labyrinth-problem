
class Board:
    players = []
    position = []
    board = []

    def draw(self):
        board = [[0, 0, 0, 2, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 0, 1, 0],
                 [0, 0, 0, 0, 0, 1, 1],
                 [1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 2, 0, 0, 0]]
        return board

    def forwards(self, x, y, board2):
        board2[x - 1][y] = '*'
        board2[x][y] = Board.draw(self)[x][y]
        return board2

    def left(self, x, y, board2):
        board2[x][y - 1] = '*'
        board2[x][y] = Board.draw(self)[x][y]
        return board2

    def right(self, x, y, board2):
        board2[x][y + 1] = '*'
        board2[x][y] = Board.draw(self)[x][y]
        return board2

    def backwards(self, x, y, board2):
        board2[x + 1][y] = '*'
        board2[x][y] = Board.draw(self)[x][y]
        return board2





