import time
import os


def clear():  # this function clears the output
    os.system('cls' if os.name == 'nt' else 'clear')
    print("")


def setupboard():  # this function produces a dictionary of the coordinates on the board
    rangerow = 1
    rangecolumn = 1
    while rangerow != maxrow + 1:
        while rangecolumn != maxcolumn + 1:
            board[str(rangecolumn) + "," + str(rangerow)] = 0
            rangecolumn += 1
        rangerow += 1
        rangecolumn = 1


def turn(player):  # this function handles the player input
    entering = True
    while entering is True:
        try:
            time.sleep(0.25)
            if player == 1:
                column = input("\nX: Choose a column: (1-" + str(maxcolumn) + "): ")
            elif player == 2:
                column = input("\nO: Choose a column: (1-" + str(maxcolumn) + "): ")
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


def falling(player, column):  # this functions makes sure that the checkers 'fall'
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


def render():  # this function converts the dictionary of coordinates and value's to something (most) humans can read
    clear()
    line1 = "    " + " " * ((len(str(maxrow))) - 1)
    rangerow = 1
    rangecolumn = 1
    while rangecolumn != maxcolumn + 1:
        line1 += str(rangecolumn) + " " * (2 + (len(str(maxcolumn))) - len(str(rangecolumn)))
        rangecolumn += 1
    print(line1)
    rangecolumn = 1
    while rangerow != maxrow + 1:
        line = " " + str(rangerow) + " " * (2 + (len(str(maxrow))) - len(str(rangerow)))
        while rangecolumn != maxcolumn + 1:
            if board[str(rangecolumn) + "," + str(rangerow)] == 0:
                line += "-" + " " * (1 + len(str(maxcolumn)))
            elif board[str(rangecolumn) + "," + str(rangerow)] == 1:
                line += "X" + " " * (1 + len(str(maxcolumn)))
            elif board[str(rangecolumn) + "," + str(rangerow)] == 2:
                line += "O" + " " * (1 + len(str(maxcolumn)))
            elif board[str(rangecolumn) + "," + str(rangerow)] == 3:
                line += " " + " " * (1 + len(str(maxcolumn)))
            else:
                print("Error")

            rangecolumn += 1
        rangerow += 1
        rangecolumn = 1
        print(line)


def winnercheck(player):  # this function checks if there is a row of four around the last checker using check()
    xy = lastturn
    x, y = xy.split(",")
    diagonaldownxy = [xy]
    verticalxy = [xy]
    diagonalupxy = [xy]
    horizontalxy = [xy]
    diagonaldown = check(diagonaldownxy, x, y, -1, -1, player) + check(diagonaldownxy, x, y, 1, 1, player)
    vertical = check(verticalxy, x, y, 0, -1, player) + check(verticalxy, x, y, 0, 1, player)
    diagonalup = check(diagonalupxy, x, y, -1, 1, player) + check(diagonalupxy, x, y, 1, -1, player)
    horizontal = check(horizontalxy, x, y, -1, 0, player) + check(horizontalxy, x, y, 1, 0, player)
    if diagonalup >= connectx - 1:
        time.sleep(0.5)
        for number in range(1, 5):
            for xy in diagonalupxy:
                board[xy] = 3
            render()
            time.sleep(0.5)
            for xy in diagonalupxy:
                board[xy] = player
                time.sleep(0.1)
                render()
            time.sleep(0.5)
        return True
    elif diagonaldown >= connectx - 1:
        time.sleep(0.5)
        for number in range(1, 5):
            for xy in diagonaldownxy:
                board[xy] = 3
            render()
            time.sleep(0.5)
            for xy in diagonaldownxy:
                board[xy] = player
                time.sleep(0.1)
                render()
            time.sleep(0.5)
        return True
    elif vertical >= connectx - 1:
        time.sleep(0.5)
        for number in range(1, 5):
            for xy in verticalxy:
                board[xy] = 3
            render()
            time.sleep(0.5)
            for xy in verticalxy:
                board[xy] = player
                time.sleep(0.1)
                render()
            time.sleep(0.5)
        return True
    elif horizontal >= connectx - 1:
        time.sleep(0.5)
        for number in range(1, 5):
            for xy in horizontalxy:
                board[xy] = 3
            render()
            time.sleep(0.5)
            for xy in horizontalxy:
                board[xy] = player
                time.sleep(0.1)
                render()
            time.sleep(0.5)
        return True


def check(linetype, x, y, offsetx, offsety, player):  # this function does the actual checking
    streak = 0
    checkx = int(x)
    checky = int(y)
    while True:
        checkx += offsetx
        checky += offsety
        try:
            if board[str(checkx) + "," + str(checky)] == player:
                streak += 1
                linetype.append(str(checkx) + "," + str(checky))
            else:
                break
        except KeyError:
            break
    return streak


while True:
    # setup
    maxrow = 7
    maxcolumn = 6
    connectx = 4
    board = {}
    setupboard()
    currentplayer = 1

    render()
    print("\nWelcome to connect four...")
    gamemode = input("Do you want to play the [CL]assic or the [CU]stom gamemode? ").lower()
    if gamemode == "cu" or gamemode == "custom":
        while True:
            try:
                maxcolumn = int(input("\nHow many columns do you want? "))
                maxrow = int(input("How many rows do you want? "))
                connectx = int(input("How many checkers must be connected to win? "))
            except ValueError:
                print("Please enter valid numbers...")
            if maxcolumn > 0 and maxrow > 0 and connectx > 0:
                break
            else:
                print("Please only enter values that are greather than zero...")
    setupboard()
    render()
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
        print("\nThe winner is 'X'")
    elif currentplayer == 2:
        print("\nThe winner is 'O'")
    playAgain = str(input("\nDo you want to play again? [Y]es or [N]o: ")).lower()
    if playAgain == "n" or playAgain == "no":
        break
