import board, pieces, ai

# Returns a move object based on the users input. Does not check if the move is valid.
def get_user_move(color = pieces.Piece.BLACK):
    print("Example Move: A2 A4")
    move_str = input("Your Move: ")
    move_str = move_str.replace(" ", "")

    try:
        if move_str == "o-o":
            if color == pieces.Piece.WHITE:
                return ai.Move(4, 0, 4+2, 0,True)
            else:
                return ai.Move(4, board.HEIGHT-1, 4+2, board.HEIGHT-1,True)
        if move_str == "O-O" or move_str == "o-o-o":
            if color == pieces.Piece.WHITE:
                return ai.Move(4, 0, 4-2, 0,True)
            else:
                return ai.Move(4, board.HEIGHT-1, 4-2, board.HEIGHT-1,True)

        xfrom = letter_to_xpos(move_str[0:1])
        yfrom = 8 - int(move_str[1:2]) # The board is drawn "upside down", so flip the y coordinate.
        xto = letter_to_xpos(move_str[2:3])
        yto = 8 - int(move_str[3:4]) # The board is drawn "upside down", so flip the y coordinate.
        return ai.Move(xfrom, yfrom, xto, yto, False)
    except ValueError:
        print("Invalid format. Example: A2 A4")
        return get_user_move(color)

# Returns a valid move based on the users input.
def get_valid_user_move(board, color = pieces.Piece.WHITE):
    while True:
        move = get_user_move(color)
        valid = False
        possible_moves = board.get_possible_moves(color)
        # No possible moves
        if (not possible_moves):
            return 0

        for possible_move in possible_moves:
            if (move.equals(possible_move)):
                valid = True
                break

        if valid:
            break
        else:
            print(move.to_string() )
            print("Invalid move.")
    return move

# Converts a letter (A-H) to the x position on the chess board.
def letter_to_xpos(letter):
    letter = letter.upper()
    if letter == 'A':
        return 0
    if letter == 'B':
        return 1
    if letter == 'C':
        return 2
    if letter == 'D':
        return 3
    if letter == 'E':
        return 4
    if letter == 'F':
        return 5
    if letter == 'G':
        return 6
    if letter == 'H':
        return 7

    raise ValueError("Invalid letter.")


def real_vs_ai():
    board_t = board.Board.new()
    print(board_t.to_string())

    while True:
        move = get_valid_user_move(board_t, pieces.Piece.WHITE)
        if (move == 0):
            if (board_t.is_check(pieces.Piece.WHITE)):
                print("Checkmate. Black Wins.")
                break
            else:
                print("Stalemate.")
                break

        board_t.perform_move(move)

        print("User move: " + move.to_string())
        print(board_t.to_string()) 
        # board_t.show()

        ai_move = ai.AI.get_ai_move(board_t, [])
        if (ai_move == 0):
            if (board_t.is_check(pieces.Piece.BLACK)):
                print("Checkmate. White wins.")
                break
            else:
                print("Stalemate.")
                break

        board_t.perform_move(ai_move)
        print("AI move: " + ai_move.to_string())
        print(board_t.to_string())


def real_vs_real():
    board_t = board.Board.new()
    print(board_t.to_string())

    while True:
        w_move = get_valid_user_move(board_t, pieces.Piece.WHITE)
        if (w_move == 0):
            if (board_t.is_check(pieces.Piece.WHITE)):
                print("Checkmate. Black Wins.")
                break
            else:
                print("Stalemate.")
                break

        board_t.perform_move(w_move)

        print("White user move: " + w_move.to_string())
        print(board_t.to_string()) 
        # board_t.show()

        b_move = get_valid_user_move(board_t, pieces.Piece.BLACK)
        if (b_move == 0):
            if (board_t.is_check(pieces.Piece.BLACK)):
                print("Checkmate. Black Wins.")
                break
            else:
                print("Stalemate.")
                break

        board_t.perform_move(b_move)

        print("Black user move: " + b_move.to_string())
        print(board_t.to_string())


def menu():
    print("Do you want to play against the AI or with your friend?")
    print("1 - AI")
    print("2 - Friend")
    val = input("Enter your value: ")

    if val == '1':
        real_vs_ai(),
    if val == '2':
        real_vs_real()
    else:
        print("Invalid Input")




#
# Entry point.
#
menu()

