

#     1  2  3  4  5  6  7
#  1  X  -  -  -  -  -  -
#  2  O  -  -  -  -  -  -
#  3  -  -  -  -  -  -  -
#  4  -  -  -  -  -  -  -
#  5  -  X  -  -  -  X  -
#  6  X  O  -  -  O  X  -

import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("")


def turn(player):
    entering = True
    while entering is True:
        print(currentplayer)
        try:
            column = input("Choose a column: (1-" + str(maxcolumn) + " ): ")
            if column == "q":
                quit()
            if board[str(int(column)) + "," + "1"] == 0:
                render()
                entering = False
                falling(player, column)
            else:
                print("This column is full")
        except ValueError and KeyError:
            render()
            print("Enter a valid number")


def falling(player, column):
    global lastturn
    fall = True
    row = 1
    while fall is True:
        board[str(column) + "," + str(row)] = player
        lastturn = str(column) + "," + str(row)
        render()
        row += 1
        if row == maxrow + 1:
            break
        elif board[str(column) + "," +str(row)] != 0:
            break
        else:
            time.sleep(0.25)
            board[str(column) + "," + str(row-1)] = 0


def render():
    clear()
    line1 = "     "
    rangerow = 1
    rangecolumn = 1
    while rangecolumn != maxcolumn +1:
        line1 += str(rangecolumn) + "  "
        rangecolumn += 1
    print(line1)
    rangecolumn = 1
    while rangerow != maxrow +1:
        line = "  " + str(rangerow) + "  "
        while rangecolumn != maxcolumn + 1:
            if board[str(rangecolumn) + "," + str(rangerow)] == 0:
                line += "-  "
            elif board[str(rangecolumn) + "," + str(rangerow)] == 1:
                line += "X  "
            elif board[str(rangecolumn) + "," + str(rangerow)] == 2:
                line += "O  "
            else:
                print("Error")

            rangecolumn += 1
        rangerow += 1
        rangecolumn = 1
        print(line)


def setupboard():
    rangerow = 1
    rangecolumn = 1
    while rangerow != maxrow +1:
        while rangecolumn != maxcolumn + 1:
            board[str(rangecolumn) + "," + str(rangerow)] = 0
            rangecolumn += 1
        rangerow += 1
        rangecolumn = 1

def winnercheck(player):
    print(lastturn)
    xy = lastturn
    x,y = xy.split(",")
#   checkleftup
    leftup = 0
    checkx = int(x)
    checky = int(y)
    print(str(checkx) + str(checky))


def check(x, y, offsetx, offsety, player):
    streak = 0
    checkx = int(x)
    checky = int(y)
    print(str(checkx) + str(checky))
    while True:
        checkx -= offsetx
        checky -= offsety
        try:
            if board[str(checkx) + "," + str(checky)] == player:
                streak += 1
            else:
                break
        except KeyError:
            break
    return streak
# setup


maxrow = 7
maxcolumn = 6
board = {}
setupboard()
currentplayer = 1

# main game loop
while True:
    render()
    turn(currentplayer)
    if winnercheck(currentplayer) is True:
        print("the winner is " + str(currentplayer))

    if currentplayer == 1:
        currentplayer = 2
    else:
        currentplayer = 1

print("Testing git")