board = {'1h': 'bking', '6c': 'wqueen',
'2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '16g': 'wbishop'}

#this is the main function that checks if the chess field is valid
def is_valid_chess_board(board):
    POSSIBLE_FIELDS = determine_possible_fields()
    print(POSSIBLE_FIELDS)


    used_fields = list(board.keys())
    print(used_fields)

    valid_field_checker(POSSIBLE_FIELDS, used_fields)

#this functions creates a list of all possible field positions from 1a to 8h
def determine_possible_fields():
    possible_fields = []
    _a_to_h = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    for letter in _a_to_h:
        for n in range(1, 9):
            possible_fields.append(str(n) + letter)
    return possible_fields

#this function checks if the currently used fields are part of all possibly valid fields
def valid_field_checker(POSSIBLE_FIELDS, used_fields):
    for field in used_fields:
        if field not in POSSIBLE_FIELDS:
            print('There is an invalid field in the game!')
            print(field + ' ' + board[field])


#this function creates a list of all


is_valid_chess_board(board)
