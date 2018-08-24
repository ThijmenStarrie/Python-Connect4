import time
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("")


def setupboard():
    rangerow = 1
    rangecolumn = 1
    while rangerow != maxrow + 1:
        while rangecolumn != maxcolumn + 1:
            board[str(rangecolumn) + "," + str(rangerow)] = 0
            rangecolumn += 1
        rangerow += 1
        rangecolumn = 1


def turn(player):
    entering = True
    while entering is True:
        try:
            time.sleep(0.25)
            column = input("\nChoose a column: (1-" + str(maxcolumn) + " ): ")
            if column == "quit":
                quit()
            if board[str(int(column)) + "," + "1"] == 0:
                render()
                entering = False
                falling(player, column)
            else:
                print("\nThis column is full")
        except ValueError:
            render()
            print("\nEnter a valid number")
        except KeyError:
            render()
            print("\nEnter a valid number")


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
        elif board[str(column) + "," + str(row)] != 0:
            break
        else:
            time.sleep(0.125)
            board[str(column) + "," + str(row-1)] = 0


def render():
    clear()
    line1 = "    "
    rangerow = 1
    rangecolumn = 1
    while rangecolumn != maxcolumn + 1:
        line1 += str(rangecolumn) + "  "
        rangecolumn += 1
    print(line1)
    rangecolumn = 1
    while rangerow != maxrow + 1:
        line = " " + str(rangerow) + "  "
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


def winnercheck(player):
    xy = lastturn
    x, y = xy.split(",")
    leftup = check(x, y, -1, -1, player)
    middleup = check(x, y, 0, -1, player)
    rightup = check(x, y, 1, -1, player)
    leftmiddle = check(x, y, -1, 0, player)
    rightmiddle = check(x, y, 1, 0, player)
    leftdown = check(x, y, -1, 1, player)
    middledown = check(x, y, 0, 1, player)
    rightdown = check(x, y, 1, 1, player)
    if leftup + rightdown >= 3:
        return True
    elif middleup + middledown >= 3:
        return True
    elif leftdown + rightup >= 3:
        return True
    elif leftmiddle + rightmiddle >= 3:
        return True


def check(x, y, offsetx, offsety, player):
    streak = 0
    checkx = int(x)
    checky = int(y)
    while True:
        checkx += offsetx
        checky += offsety
        try:
            if board[str(checkx) + "," + str(checky)] == player:
                streak += 1
            else:
                break
        except KeyError:
            break
    return streak


while True:
    # setup
    maxrow = 7
    maxcolumn = 6
    board = {}
    setupboard()
    currentplayer = 1

    render()
    print("\nWelcome to connect four...")
    time.sleep(0.50)
    print("\nEnter the number of the column you want to drop your checkers in...")

    while True:  # main game loop
        turn(currentplayer)
        if winnercheck(currentplayer) is True:
            break
        if currentplayer == 1:
            currentplayer = 2
        else:
            currentplayer = 1
        render()

    if currentplayer == 1:
        print("\nThe winner is 'x'")
    elif currentplayer == 2:
        print("\nThe winner is 'O'")
    playAgain = str(input("\nDo you want to play again? [Y]es or [N]o: ")).lower()
    if playAgain == "n" or playAgain == "no":
        break
