#
#    Algorithm:
# 1. Print an empty field.
# 2. The beginning of the cycle: who goes?
# 3. User enters coordinates.
# 4. Input analysis: if correct, next step; if not, go to step 3.
# 5. Result analysis: draw, x won, o won, continue playing.
#    If the game continues, go to step 2. Otherwise, the game is over.

s = [" " for cell in range(9)]  # empty field

row_up = s[0] + s[1] + s[2]
row_mid = s[3] + s[4] + s[5]
row_bot = s[6] + s[7] + s[8]

column_left = s[0] + s[3] + s[6]
column_mid = s[1] + s[4] + s[7]
column_right = s[2] + s[5] + s[8]

diagonal_left_right = s[0] + s[4] + s[8]
diagonal_right_left = s[2] + s[4] + s[6]

rows_columns_diags = [
    row_up,
    row_mid,
    row_bot,
    column_left,
    column_mid,
    column_right,
    diagonal_left_right,
    diagonal_right_left
]


def update_rows_columns_diags():
    global row_up, row_mid, row_bot, column_left, column_mid, column_right, diagonal_left_right, diagonal_right_left,\
        rows_columns_diags
    # What is rows, columns and diagonals:
    row_up = s[0] + s[1] + s[2]
    row_mid = s[3] + s[4] + s[5]
    row_bot = s[6] + s[7] + s[8]

    column_left = s[0] + s[3] + s[6]
    column_mid = s[1] + s[4] + s[7]
    column_right = s[2] + s[5] + s[8]

    diagonal_left_right = s[0] + s[4] + s[8]
    diagonal_right_left = s[2] + s[4] + s[6]

    rows_columns_diags = [
        row_up,
        row_mid,
        row_bot,
        column_left,
        column_mid,
        column_right,
        diagonal_left_right,
        diagonal_right_left
    ]


def print_field():
    print('---------')
    print('|', s[0], s[1], s[2], '|')
    print('|', s[3], s[4], s[5], '|')
    print('|', s[6], s[7], s[8], '|')
    print('---------')


def input_x_coords():
    global x_goes
    has_the_coords_been_entered = False
    while not has_the_coords_been_entered:
        try:
            coords = input("Enter the coordinates: > ").split()
            if coords[0].isdecimal() and coords[1].isdecimal():  # check if user entered decimal numbers or other
                                                                 # characters
                if coords[0] in ['1', '2', '3'] and coords[1] in ['1', '2', '3']:  # check out of the field
                    if coords == ['1', '1'] and s[6] == ' ':  # if the cell is not busy,
                        s[6] = 'X'  # write “X” there,
                        has_the_coords_been_entered = True  # note that the input was successful
                    elif coords == ['2', '1'] and s[7] == ' ':
                        s[7] = 'X'
                        has_the_coords_been_entered = True
                    elif coords == ['3', '1'] and s[8] == ' ':
                        s[8] = 'X'
                        has_the_coords_been_entered = True
                    elif coords == ['1', '2'] and s[3] == ' ':
                        s[3] = 'X'
                        has_the_coords_been_entered = True
                    elif coords == ['2', '2'] and s[4] == ' ':
                        s[4] = 'X'
                        has_the_coords_been_entered = True
                    elif coords == ['3', '2'] and s[5] == ' ':
                        s[5] = 'X'
                        has_the_coords_been_entered = True
                    elif coords == ['1', '3'] and s[0] == ' ':
                        s[0] = 'X'
                        has_the_coords_been_entered = True
                    elif coords == ['2', '3'] and s[1] == ' ':
                        s[1] = 'X'
                        has_the_coords_been_entered = True
                    elif coords == ['3', '3'] and s[2] == ' ':
                        s[2] = 'X'
                        has_the_coords_been_entered = True
                    else:
                        print("This cell is occupied! Choose another one!")
                        continue
                else:
                    print("Coordinates should be from 1 to 3!")
                continue
            else:
                print("You should enter numbers!")
                continue
        except IndexError:
            print("You should enter numbers!")
            continue
    x_goes = False


def input_o_coords():
    global x_goes
    has_the_coords_been_entered = False
    while not has_the_coords_been_entered:
        try:
            coords = input("Enter the coordinates: > ").split()
            if coords[0].isdecimal() and coords[1].isdecimal():  # check if user entered decimal numbers or other
                                                                 # characters
                if coords[0] in ['1', '2', '3'] and coords[1] in ['1', '2', '3']:  # check out of the field
                    if coords == ['1', '1'] and s[6] == ' ':  # if the cell is not busy,
                        s[6] = 'O'  # write “O” there,
                        has_the_coords_been_entered = True  # note that the input was successful
                    elif coords == ['2', '1'] and s[7] == ' ':
                        s[7] = 'O'
                        has_the_coords_been_entered = True
                    elif coords == ['3', '1'] and s[8] == ' ':
                        s[8] = 'O'
                        has_the_coords_been_entered = True
                    elif coords == ['1', '2'] and s[3] == ' ':
                        s[3] = 'O'
                        has_the_coords_been_entered = True
                    elif coords == ['2', '2'] and s[4] == ' ':
                        s[4] = 'O'
                        has_the_coords_been_entered = True
                    elif coords == ['3', '2'] and s[5] == ' ':
                        s[5] = 'O'
                        has_the_coords_been_entered = True
                    elif coords == ['1', '3'] and s[0] == ' ':
                        s[0] = 'O'
                        has_the_coords_been_entered = True
                    elif coords == ['2', '3'] and s[1] == ' ':
                        s[1] = 'O'
                        has_the_coords_been_entered = True
                    elif coords == ['3', '3'] and s[2] == ' ':
                        s[2] = 'O'
                        has_the_coords_been_entered = True
                    else:
                        print("This cell is occupied! Choose another one!")
                        continue
                else:
                    print("Coordinates should be from 1 to 3!")
                    continue
            else:
                print("You should enter numbers!")
                continue
        except IndexError:
            print("You should enter numbers!")
            continue                              
    x_goes = True


def result_analysis():
    global game_over
    update_rows_columns_diags()
    if ('XXX' not in rows_columns_diags and 'OOO' not in rows_columns_diags) and ' ' not in s:
        print("Draw")  # when no side has a three in a row and the field has no empty cells;
        game_over = True
    elif 'XXX' in rows_columns_diags and 'OOO' not in rows_columns_diags:
        print("X wins")  # when the field has three X in a row;
        game_over = True
    elif 'XXX' not in rows_columns_diags and 'OOO' in rows_columns_diags:
        print("O wins")  # when the field has three O in a row;
        game_over = True


print_field()  # here the field is empty yet

x_goes = True
game_over = False

while not game_over:
    if x_goes:
        input_x_coords()
    else:
        input_o_coords()
    print_field()
    result_analysis()
