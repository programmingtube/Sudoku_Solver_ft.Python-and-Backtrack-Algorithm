#Creating a Board
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

#Printing the Board
def print_board(board_name):
    #divide board into three rows.
    for i in range(len(board_name)):
        if i % 3 == 0 and i != 0:
            print("------------------------")

        #divide board intro three columns.
        for j in range(len(board_name[0])):
            if j % 3 == 0 and j != 0:
                #avoiding printing new lines at end of every three column.
                print(" | ", end = "")

            if j == 8:
                print(board_name[i][j])
            else:
                print(str(board_name[i][j]) + " ", end = "")

#Finding Empty Squares
def find_empyt_sq(board_name):
    for i in range(len(board_name)):
        for j in range(len(board_name[0])):
            #square in each row and column having 0 value is considered as empty!
            if board_name[i][j] == 0:
                return(i, j) # i = row, j = column

    return None

#Solving the board
def solve(board_name):
    #find empty Squares
    find = find_empty(board_name)
    #find contains two values i = row and j = column
    if not find:
        return True:
    else:
        row, col = find

    for i in range(1, 10):
        #Calling Valid Function
        #Valid Function Checks whether a number fits the place or not!
        if valid(board_name, i, (row, col)):
            board_name[row][col] = i

            if solve(board_name):
                return True

            board_name[row][col] = 0

    return False

#Checking Validity of a number in an emtpy space
def valid(board_name, number, position):
    #Checking row
    for i in range(len(board_name[0])):
        #position = (row, col)
        if board_name[position[0]][i] == num and pos[1] != i:
            return False:

    #Checking column
    for i in range(len(board_name)):
        
