
def current_user(user):
    if user:
        return "x"
    else:
        return "o"

def add_to_board(user ,coords ,board):
    row =coords[0]
    col =coords[1]
    board[row][col ] =current_user(user)


def print_board(board):
    for row in board:
        for slot in row:
            print(f"{slot}" ,end=" ")
        print()
def quit(user_input):
    if user_input=="q":
        print('Thanks for playing')
        return True
    else:
        return False


def check_input(user_input):
    if not user_input.isnumeric():
        print("Only numbers are allowed")
        return False
    return True

def bounds(user_input):
    user_input =int(user_input)
    if user_input >9 or user_input <1:
        print("out of range")
        return False
    else:
        return True

def istaken(coords ,board):
    row =coords[0]
    col =coords[1]
    if board[row][col]!="-":
        print("position already taken")
        return False
    return True


def coordinates(user_input):
    row =int(user_input /3)
    col =user_input
    if col >2 :col =int(col %3)
    return (row ,col)

def check_row(active_user ,board):

    for row in board:
        row_completed =True
        for slot in row:
            if slot!=active_user:
                row_completed= False
                break
        if row_completed:
            return True
    return False

def check_col(active_user ,board):
    for col in range(3):
        col_completed =True
        for row in range(3):
            if board[row][col]!=active_user:
                col_completed =False
                break
        if col_completed :return True
    return False


def check_dig(active_user ,board):
    if (board[0][0]==active_user and board[1][1]==active_user and
            board[2][2]==active_user):
        return True
    elif (board[0][2]==active_user and board[1][1]==active_user and
          board[2][0]==active_user):
        return True
    return False






def iswin(active_user ,board):
    if check_row(active_user ,board) :return True
    if check_col(active_user ,board) :return True
    if check_dig(active_user ,board) :return True

def play():
    board =[
        ["-" ,"-" ,"-"],
        ["-" ,"-" ,"-"],
        ["-" ,"-" ,"-"]]
    turns =0
    user =True

    while turns <9  :  # max entries can be 9
        active_user =current_user(user)
        turns+=0
        print_board(board)
        user_input =input("choose position\nbetween 1to9 or\"q\" to quit")

        if quit(user_input) :break

        if not check_input(user_input):
            print("try again")
            continue
        if not bounds(user_input):
            print("try again")
            continue
        user_input =int(user_input ) -1
        coords =coordinates(user_input)
        if not istaken(coords ,board):
            continue
        add_to_board(user ,coords ,board)
        if iswin(active_user ,board):
            print(f"{active_user.upper()} win😀!!!")
            break
        if turns==9 :print("Tie🙁")

        user= not user





print("Welcome😍 to the Tic-Tac-Toe made by SASKE!!!")
play()
a= input('Do you want to\nplay again.Press \"y\" for yes\n\"n\" for no')
if (a == 'y'): play()
