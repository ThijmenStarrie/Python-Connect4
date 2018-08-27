import time
import os


def clear_console_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("")


def setup_board():  # this function produces a dictionary of the coordinates on the board
    range_row = 1
    range_column = 1
    setup = {}
    while range_row != max_row + 1:
        while range_column != max_column + 1:
            setup[str(range_column) + "," + str(range_row)] = 0
            range_column += 1
        range_row += 1
        range_column = 1
    return setup


def player_input(player):  # this function handles the player input
    entering = True
    global restart
    while entering is True:
        try:
            time.sleep(0.25)
            if player == 1:
                column = input("X: Choose a column: (1-" + str(max_column) + "): ")
            elif player == 2:
                column = input("O: Choose a column: (1-" + str(max_column) + "): ")
            if column == "quit":
                quit()
            elif column == "restart":
                restart = True
                break
            if board[str(int(column)) + "," + "1"] == 0:
                render_dict()
                entering = False
                falling_animation(player, column)
            else:
                print("\nThis column is full")
        except ValueError:
            render_dict()
            print("\nEnter a valid number")
        except KeyError:
            render_dict()
            print("\nEnter a valid number")


def falling_animation(player, column):  # this functions makes sure that the checkers 'fall'
    global last_turn
    fall = True
    row = 1
    while fall is True:
        board[str(column) + "," + str(row)] = player
        last_turn = str(column) + "," + str(row)
        if falling_toggle is True:
            render_dict()
        row += 1
        if row == max_row + 1:
            break
        elif board[str(column) + "," + str(row)] != 0:
            break
        else:
            if falling_toggle is True:
                time.sleep(0.125)
            board[str(column) + "," + str(row-1)] = 0


def render_dict():  #
    clear_console_screen()
    line1 = "    " + " " * ((len(str(max_row))) - 1)
    range_row = 1
    range_column = 1
    while range_column != max_column + 1:
        line1 += str(range_column) + " " * (2 + (len(str(max_column))) - len(str(range_column)))
        range_column += 1
    print(line1)
    range_column = 1
    while range_row != max_row + 1:
        line = " " + str(range_row) + " " * (2 + (len(str(max_row))) - len(str(range_row)))
        while range_column != max_column + 1:
            if board[str(range_column) + "," + str(range_row)] == 0:
                line += "-" + " " * (1 + len(str(max_column)))
            elif board[str(range_column) + "," + str(range_row)] == 1:
                line += "X" + " " * (1 + len(str(max_column)))
            elif board[str(range_column) + "," + str(range_row)] == 2:
                line += "O" + " " * (1 + len(str(max_column)))
            elif board[str(range_column) + "," + str(range_row)] == 3:
                line += " " + " " * (1 + len(str(max_column)))
            else:
                print("Error")

            range_column += 1
        range_row += 1
        range_column = 1
        print(line)
    print()


def check_for_winner(player):
    xy = last_turn
    x, y = xy.split(",")
    diagonal_down_xy = [xy]
    vertical_xy = [xy]
    diagonal_up_xy = [xy]
    horizontal_xy = [xy]
    diagonal_down = check_xy(diagonal_down_xy, x, y, -1, -1, player) + check_xy(diagonal_down_xy, x, y, 1, 1, player)
    vertical = check_xy(vertical_xy, x, y, 0, -1, player) + check_xy(vertical_xy, x, y, 0, 1, player)
    diagonal_up = check_xy(diagonal_up_xy, x, y, -1, 1, player) + check_xy(diagonal_up_xy, x, y, 1, -1, player)
    horizontal = check_xy(horizontal_xy, x, y, -1, 0, player) + check_xy(horizontal_xy, x, y, 1, 0, player)
    if diagonal_up >= connect_x - 1:
        for number in range(1, 4):
            for xy in diagonal_up_xy:
                board[xy] = 3
            render_dict()
            time.sleep(0.4)
            for xy in diagonal_up_xy:
                board[xy] = player
            render_dict()
            time.sleep(0.4)
        return True
    elif diagonal_down >= connect_x - 1:
        for number in range(1, 4):
            for xy in diagonal_down_xy:
                board[xy] = 3
            render_dict()
            time.sleep(0.4)
            for xy in diagonal_down_xy:
                board[xy] = player
            render_dict()
            time.sleep(0.4)
        return True
    elif vertical >= connect_x - 1:
        for number in range(1, 4):
            for xy in vertical_xy:
                board[xy] = 3
            render_dict()
            time.sleep(0.4)
            for xy in vertical_xy:
                board[xy] = player
            render_dict()
            time.sleep(0.4)
        return True
    elif horizontal >= connect_x - 1:
        for number in range(1, 4):
            for xy in horizontal_xy:
                board[xy] = 3
            render_dict()
            time.sleep(0.4)
            for xy in horizontal_xy:
                board[xy] = player
            render_dict()
            time.sleep(0.4)
        return True


def check_xy(line_type, x, y, offset_x, offset_y, player):  # this function does the actual checking
    streak = 0
    check_x = int(x)
    check_y = int(y)
    while True:
        check_x += offset_x
        check_y += offset_y
        try:
            if board[str(check_x) + "," + str(check_y)] == player:
                streak += 1
                line_type.append(str(check_x) + "," + str(check_y))
            else:
                print()
                break
        except KeyError:
            break
    return streak


while True:
    # setup
    max_row = 7
    max_column = 6
    connect_x = 4
    current_player = 1
    board = setup_board()
    falling_toggle = True
    restart = False

    render_dict()
    print("Welcome to connect four...\n")
    game_mode = input("Do you want to play the [CL]assic or the [CU]stom gamemode? ").lower()
    if game_mode == "cu" or game_mode == "custom":
        while True:
            while True:
                try:
                    max_column = int(input("How many columns do you want? "))
                    max_row = int(input("How many rows do you want? "))
                    connect_x = int(input("How many checkers must be connected to win? "))
                    falling_toggle = str(input("Do you want to enable the falling animation? [Y]es or [N]o: ")).lower()
                except ValueError:
                    print("Please enter valid numbers...\n")
                else:
                    break
            if falling_toggle == "n" or "no":
                falling_toggle = False
            if max_column > 0 and max_row > 0 and connect_x > 0:
                break
            else:
                print("Please only enter values that are greater than zero...\n")
        board = setup_board()

    render_dict()
    time.sleep(0.50)
    print("Enter the number of the column you want to drop your checkers in...\n")

    while True:  # main game loop
        player_input(current_player)
        if restart is True:
            break
        if check_for_winner(current_player) is True:
            break
        if current_player == 1:
            current_player = 2
        else:
            current_player = 1
        render_dict()
    if restart is True:
        continue
    if current_player == 1:
        print("The winner is 'X'\n")
    elif current_player == 2:
        print("The winner is 'O'\n")
    play_again = str(input("Do you want to play again? [Y]es or [N]o: ")).lower()
    if play_again == "n" or play_again == "no":
        break
