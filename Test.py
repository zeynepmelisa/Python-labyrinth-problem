# Position Class -> x, y
#                -> __init__(), __str__()
# Board Class -> class board, class players=[], class position=[]
#             -> draw(), forwards(), left(), right(), backwards()
# Test -> points=0

from board import Board
from position import Position

board = Board()
for x in range(8):
    for y in range(7):
        position = Position(x, y)
        board.position.append([x, y])


for line in board.draw():
    print(line)

not_end = True
player0 = Position(7, 3)
board.players.append(player0)
board2 = board.draw().copy()
board2[player0.x][player0.y] = '*'
print()
for line in board2:
    print(line)

print("Let's the game begin!")

while not_end:
    option = input("Which direction do you want to go? (F-forwards/ L-left/ R-right/ B-backwards)  ")
    if option == 'F':
        # if board2[player0.x - 1][player0.y] != 1:
        #     board2[player0.x][player0.y] = board.draw()[player0.x][player0.y]
        #     player0.x = player0.x - 1
        #     board2[player0.x][player0.y] = '*'
        #     for line in board2:
        #         print(line)
        # else:
        #     print("Game over!")
        #     not_end = False

        if board.draw()[player0.x - 1][player0.y] != 1:
            board2 = board.draw().copy()
            for line in board.forwards(player0.x, player0.y, board2):
                print(line)
            player0.x = player0.x - 1
        else:
            print("Game over!")
            not_end = False

    elif option == 'L':
        # if board2[player0.x][player0.y - 1] != 1:
        #     board2[player0.x][player0.y] = board.draw()[player0.x][player0.y]
        #     player0.y = player0.y - 1
        #     board2[player0.x][player0.y] = '*'
        #     for line in board2:
        #         print(line)
        # else:
        #     print("Game over!")
        #     not_end = False
        if board.draw()[player0.x][player0.y - 1] != 1:
            for line in board.left(player0.x, player0.y, board2):
                print(line)
            player0.y = player0.y - 1
        else:
            print("Game over!")
            not_end = False

    elif option == 'R':
        # if board2[player0.x][player0.y + 1] != 1:
        #     board2[player0.x][player0.y] = board.draw()[player0.x][player0.y]
        #     player0.y = player0.y + 1
        #     board2[player0.x][player0.y] = '*'
        #     for line in board2:
        #         print(line)
        # else:
        #     print("Game over!")
        #     not_end = False
        if board.draw()[player0.x][player0.y + 1] != 1:
            for line in board.right(player0.x, player0.y, board2):
                print(line)
            player0.y = player0.y + 1
        else:
            print("Game over!")
            not_end = False

    elif option == 'B':
        # if player0.x != 7:
        #     if board2[player0.x + 1][player0.y] != 1:
        #         board2[player0.x][player0.y] = board.draw()[player0.x][player0.y]
        #         player0.y = player0.y + 1
        #         board2[player0.x][player0.y] = '*'
        #         for line in board2:
        #             print(line)
        #     else:
        #         print("Game over!")
        #         not_end = False
        # else:
        #     print("This move is not possible yet!")
        if player0.x != 7:
            if board.draw()[player0.x + 1][player0.y] != 1:
                for line in board.backwards(player0.x, player0.y, board2):
                    print(line)
                player0.x = player0.x + 1
            else:
                print("Game over!")
                not_end = False
        else:
            print("This move is not possible yet!")

    else:
        print("Wrong option!")

    if player0.x == 0 and player0.y == 3:
        print("Congratulations!")
        not_end = False





