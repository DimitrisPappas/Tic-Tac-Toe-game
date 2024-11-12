###   Milestone Project 1   ###

print("---   Milestone Project 1   ---")

def display_tictactoe_screen(matrix):
    '''
    Get a dictionary that represent a 3x3 matrix and print the 3x3 grid of tic tac toe
    :param matrix: dictionary
    :return: print
    '''
    # print("\n" * 100)
    print("\n")
    print(f" {matrix["00"]} | {matrix["01"]} | {matrix["02"]} ")
    print("-----------")
    print(f" {matrix["10"]} | {matrix["11"]} | {matrix["12"]} ")
    print("-----------")
    print(f" {matrix["20"]} | {matrix["21"]} | {matrix["22"]} ")
    print("\n")


def starting_symbol_choice():
    '''
    Ask player 1 to choose their starting symbol 'X' or 'O'
    :return: (char,char) starting symbol for each player
    '''
    symbolChoice = ""
    symbolOptions = ['X','O','x','o']
    invalidSymbol = True
    while invalidSymbol:
        symbolChoice = input("Player 1 choose your symbol: X or O ")
        if symbolChoice not in symbolOptions:
            print("Ivalid symbol")
            continue
        else:
            symbolChoice = symbolChoice.upper()
            invalidSymbol = False
    print(f"Player 1 is playing: {symbolChoice}")
    if symbolChoice == "X":
        otherSymbol = "O"
    else:
        otherSymbol = "X"
    print(f"Player 2 is playing: {otherSymbol}")
    print("\n")
    return (symbolChoice,otherSymbol)


def player_position_choice(positionOptions):
    '''
    Ask player to choose the position to place their symbol
    :param positionOptions: available positions
    :return: (str) position
    '''
    invalidPosition = True
    while invalidPosition:
        positionChoice = input(f"Choose the position to place your symbol:\n00, 01, 02\n10, 11, 12\n20, 21, 22\nAvailable positions: {positionOptions}\n")
        if positionChoice not in positionOptions:       # check for free positions
            print("Invalid position")
            continue
        else:
            invalidPosition = False
    return positionChoice


def check_3_connected_same_symbols(positions, lastMove, playerSymbol):
    '''
    Ckeck for 3 connected same symbols in each row, column and diagonal
    :param positions: position directory matrix
    :param lastMove: player's last move
    :param playerSymbol: player'd symbol
    :return: (bool) True if win-endgame / False if continue playing
    '''
    if lastMove[0] == "0":
        if lastMove[1] == "0":      # 00
            if positions["01"] == playerSymbol and positions["02"] == playerSymbol:
                return True
            elif positions["10"] == playerSymbol and positions["20"] == playerSymbol:
                return True
            elif positions["11"] == playerSymbol and positions["22"] == playerSymbol:
                return True
            else:
                return False
        if lastMove[1] == "1":      # 01
            if positions["00"] == playerSymbol and positions["02"] == playerSymbol:
                return True
            elif positions["11"] == playerSymbol and positions["21"] == playerSymbol:
                return True
            else:
                return False
        if lastMove[1] == "2":      # 02
            if positions["00"] == playerSymbol and positions["01"] == playerSymbol:
                return True
            elif positions["12"] == playerSymbol and positions["22"] == playerSymbol:
                return True
            elif positions["11"] == playerSymbol and positions["20"] == playerSymbol:
                return True
            else:
                return False
    elif lastMove[0] == "1":
        if lastMove[1] == "0":      # 10
            if positions["11"] == playerSymbol and positions["12"] == playerSymbol:
                return True
            elif positions["00"] == playerSymbol and positions["20"] == playerSymbol:
                return True
            else:
                return False
        if lastMove[1] == "1":      # 11
            if positions["10"] == playerSymbol and positions["12"] == playerSymbol:
                return True
            elif positions["01"] == playerSymbol and positions["21"] == playerSymbol:
                return True
            elif positions["00"] == playerSymbol and positions["22"] == playerSymbol:
                return True
            elif positions["02"] == playerSymbol and positions["20"] == playerSymbol:
                return True
            else:
                return False
        if lastMove[1] == "2":      # 12
            if positions["10"] == playerSymbol and positions["11"] == playerSymbol:
                return True
            elif positions["02"] == playerSymbol and positions["22"] == playerSymbol:
                return True
            else:
                return False
    elif lastMove[0] == "2":
        if lastMove[1] == "0":      # 20
            if positions["21"] == playerSymbol and positions["22"] == playerSymbol:
                return True
            elif positions["00"] == playerSymbol and positions["10"] == playerSymbol:
                return True
            elif positions["11"] == playerSymbol and positions["02"] == playerSymbol:
                return True
            else:
                return False
        if lastMove[1] == "1":      # 21
            if positions["20"] == playerSymbol and positions["22"] == playerSymbol:
                return True
            elif positions["01"] == playerSymbol and positions["11"] == playerSymbol:
                return True
            else:
                return False
        if lastMove[1] == "2":      # 22
            if positions["20"] == playerSymbol and positions["21"] == playerSymbol:
                return True
            elif positions["02"] == playerSymbol and positions["12"] == playerSymbol:
                return True
            elif positions["00"] == playerSymbol and positions["11"] == playerSymbol:
                return True
            else:
                return False
    else:
        print("Symbol position out of bounds")
        return False


def tictactoe_game():
    '''
    Play Tic Tac Toe game
    :return: (int) 0: tie, 1, Player 1 won, 2: player 2 won
    '''
    # Dictionary with positions and symbols, e.g. {"00": "X"}. Represents the game matrix.
    positions = {"00": " ", "01": " ", "02": " ", "10": " ", "11": " ", "12": " ", "20": " ", "21": " ", "22": " "}
    # List with the available positions to place symbol
    positionOptions = ["00", "01", "02", "10", "11", "12", "20", "21", "22"]
    display_tictactoe_screen(positions)         # Display initial game screen
    (player_1_symbol, player_2_symbol) = starting_symbol_choice()   # Ask Player 1 to choose symbol
    winner = 0      # Tie
    turn = 1        # current turn
    gameOn = True
    while gameOn:
        print(f"~~ Turn {turn} ~~")
        print(" - Player 1 - ")
        player_1_position = player_position_choice(positionOptions) # ask Player 1 to choose the position to place their symbol
        positionOptions.remove(player_1_position)                   # remove used position
        # print(positionOptions)
        positions[player_1_position] = player_1_symbol              # update game matrix with player 1 choice
        display_tictactoe_screen(positions)
        if check_3_connected_same_symbols(positions,player_1_position,player_1_symbol): # check if player 1 won
            winner = 1  # Player 1 won
            gameOn = False
        turn += 1
        if turn == 10: # full game matrix
            gameOn = False
        if gameOn:  # Player 1 did not win with last move
            print(f"~~ Turn {turn} ~~")
            print(" - Player 2 - ")
            player_2_position = player_position_choice(positionOptions) # ask Player 2 to choose the position to place their symbol
            positionOptions.remove(player_2_position)                   # remove used position
            print(positionOptions)
            positions[player_2_position] = player_2_symbol              # update game matrix with player 2 choice
            display_tictactoe_screen(positions)
            if check_3_connected_same_symbols(positions,player_2_position,player_2_symbol): # check if player 2 won
                winner = 2  # Player 2 won
                gameOn = False
            turn += 1
    return winner


def game_outcome(winner):
    '''
    Print winner
    :param winner: 0: Tie, 1: player 1 won, 2: player 2 won
    :return:
    '''
    if winner == 0:
        print("Tie")
    elif winner == 1:
        print("Player 1 WON")
    elif winner == 2:
        print("Player 2 WON")
    else:
        print("Error")
    print("Thank you for playing!")


def replay_game():
    '''
    Ask players if they wish to replay the game
    :return: bool
    '''
    replayOptions = ["Yes","No","yes","no","y","n","Y","N","YES","NO"]
    replayYES = ["Yes","yes","y","Y","YES"]
    invalidReplayChoice = True
    while invalidReplayChoice:
        replay = input("\nReplay? Yes or No ")
        if replay in replayOptions:
            invalidReplayChoice = False
    return replay in replayYES


# MAIN
replay = True
while replay:
    winner = tictactoe_game()
    game_outcome(winner)
    replay = replay_game()
