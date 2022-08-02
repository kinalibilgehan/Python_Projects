grid = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
x_list = []
o_list = []

winning_combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [
    1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]


def starter_settings():
    global grid
    global x_list
    global o_list
    grid = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
    x_list = []
    o_list = []


def display_board():
    global grid
    print(grid[0] + " | " + grid[1] + " | " + grid[2])
    print(".........")
    print(grid[3] + " | " + grid[4] + " | " + grid[5])
    print(".........")
    print(grid[6] + " | " + grid[7] + " | " + grid[8])
    print(".........")


def player_1():
    player_1_choice = input("Player1: Where do you want to put 'X' ?: ")
    x_list.append(int(player_1_choice))
    grid[int(player_1_choice) - 1] = "X"
    print(x_list)
    display_board()


def player_2():
    player_2_choice = input("Player 2: Where do you want to put 'O' ?: ")
    o_list.append(int(player_2_choice))
    grid[int(player_2_choice) - 1] = "O"
    display_board()


def check_win():
    if "_" not in grid:
        print("It's a draw")
        return True
    if sorted(x_list) in winning_combinations:
        print("Player 1 Wins")
        return True
    elif sorted(o_list) in winning_combinations:
        print("Player 2 Wins")
        return True
    else:
        return False


def play_again():

    another_round = input(
        "Do you want to play again? 'y' for yes 'n' for no: ")
    if another_round == "y":
        return True
    else:
        return False


def play_game():

    print("Game Board is numbered from 1 to 9. Select where you want to make your move.")

    starter_settings()

    game_is_on = True

    while game_is_on:
        display_board()
        player_1()
        if check_win():
            if play_again():
                play_game()
            else:
                game_is_on = False
        player_2()
        if check_win():
            if play_again():
                play_game()
            else:
                game_is_on = False


play_game()
