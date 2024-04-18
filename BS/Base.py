# 1. tictactoe
board_list = [['-', '-', '-'], ['-', '-', '-'], ['-', '-' , '-']]
turn = 'x'
count = 1

for i in range(0, 3):
    for j in range(0, 3):
        print(board_list[i][j], end=" ")
    #
    print()
#
print()

while(count <= 9):

    # taking user input
    print("***** " + turn + "'s turn *****")
    row = int(input("Enter row value: "))
    col = int(input("Enter column value: "))

    # logic for checking acquired positions
    if board_list[row-1][col-1] != '-':
        print("\nPosition already acquired! Please take another position\n")
        continue
    else:
        count += 1
    #
    print()

    # assigning the position to respective player
    if count%2 == 0:
        board_list[row-1][col-1] = turn
    else:
        board_list[row-1][col-1] = turn
    #
        
    # printing the current phase
    for i in range(0, 3):
        for j in range(0, 3):
            print(board_list[i][j], end=" ")
        #
        print()
    #
    print()       
    
    # checking for winner
    flag = 0
    if count > 5:
        if board_list[0][0] == board_list[0][1] == board_list[0][2] != '-':
            print("Congratulations, " + turn + " Won!")
            flag = 1
        elif board_list[1][0] == board_list[1][1] == board_list[1][2] != '-':
            print("Congratulations, " + turn + " Won!")
            flag = 1
        elif board_list[2][0] == board_list[2][1] == board_list[2][2] != '-':
            print("Congratulations, " + turn + " Won!")
            flag = 1
        elif board_list[0][0] == board_list[1][0] == board_list[2][0] != '-':
            print("Congratulations, " + turn + " Won!")
            flag = 1
        elif board_list[0][1] == board_list[1][1] == board_list[2][1] != '-':
            print("Congratulations, " + turn + " Won!")
            flag = 1
        elif board_list[0][2] == board_list[1][2] == board_list[2][2] != '-':
            print("Congratulations, " + turn + " Won!")
            flag = 1
        elif board_list[0][0] == board_list[1][1] == board_list[2][2] != '-':
            print("Congratulations, " + turn + " Won!")
            flag = 1
        elif board_list[0][2] == board_list[1][1] == board_list[2][0] != '-':
            print("Congratulations, " + turn + " Won!")
            flag = 1
        #
    #
    
    # checking for tie
    if count == 9 and flag == 0:
        print("It's a tie")
        flag = 1
    #
    
    if flag:
        con = input("Do you want to continue? y/n: ")
        if con == 'y' or con == 'Y':
            count = 0
            # resetting the positions
            for i in range(0, 3):
                for j in range(0, 3):
                    board_list[i][j] = '-'
                #
            #
            print()
            continue
        else:
            break
        #
    #    
    
    if turn == 'x':
        turn = 'o'
    else:
        turn = 'x'

# 2. 8 Puzzle problem in AI.

def print_in_format(matrix):
    for i in range(9):
        if i % 3 == 0 and i > 0:
            print("")
        print(str(matrix[i])+" ", end="")


def count(s):
    c = 0
    ideal = [1, 2, 3,
             4, 5, 6,
             7, 8, 0] 

    for i in range(9):
        if s[i] != 0 and s[i] != ideal[i]:
            c += 1
    return c


def move(ar, p, st): 
    rh = 9999
    store_st = st.copy()

    for i in range(len(ar)): 

        dupl_st = st.copy()

        tmp = dupl_st[p]    
        dupl_st[p] = dupl_st[ar[i]]   
        dupl_st[ar[i]] = tmp  
	
        trh = count(dupl_st)

        if trh < rh:
            rh = trh
            store_st = dupl_st.copy()

    # print(rh, store_st)

    return store_st, rh


state = [1, 2, 3,
         0, 5, 6,
         4, 7, 8]

h = count(state)
Level = 1

print("\n------ Level "+str(Level)+" ------")
print_in_format(state)
print("\nHeuristic Value(Misplaced) : "+str(h))


while h > 0:
    pos = int(state.index(0))

    Level += 1

    if pos == 0:
        arr = [1, 3]
        state, h = move(arr, pos, state)
    elif pos == 1:
        arr = [0, 2, 4]
        state, h = move(arr, pos, state)
    elif pos == 2:
        arr = [1, 5]
        state, h = move(arr, pos, state)
    elif pos == 3:
        arr = [0, 4, 6]
        state, h = move(arr, pos, state)
    elif pos == 4:
        arr = [1, 3, 5, 7]
        state, h = move(arr, pos, state)
    elif pos == 5:
        arr = [2, 4, 8]
        state, h = move(arr, pos, state)
    elif pos == 6:
        arr = [3, 7]
        state, h = move(arr, pos, state)
    elif pos == 7:
        arr = [4, 6, 8]
        state, h = move(arr, pos, state)
    elif pos == 8:
        arr = [5, 7]
        state, h = move(arr, pos, state)

    print("\n------ Level "+str(Level)+" ------")
    print_in_format(state)
    print("\nHeuristic Value(Misplaced) : "+str(h))

# 3. Water jug problem
a = int(input("Enter Jug A Capacity: "))
b = int(input("Enter Jug B ")); 
ai = int(input("Initially Water in Jug A: "))
bi = int(input("Initially Water in Jug B: "))
af = int(input("Final State of Jug A: "))
bf = int(input("Final State of Jug B: "))

print("List Of Operations You can Do:\n")
print("1. Fill Jug A Completely\n")
print("2. Fill Jug B Completely\n")
print("3. Empty Jug A Completely\n")
print("4. Empty Jug B Completely\n")
print("5. Pour From Jug A till Jug B filled Completely or A becomes empty\n")
print("6. Pour From Jug B till Jug A filled Completely or B becomes empty\n")
print("7. Pour all From Jug B to Jug A\n")
print("8. Pour all From Jug A to Jug B\n")

while ((ai != af or bi != bf)):
    op = int(input("Enter the operation: "))
    if(op == 1):
        ai = a
    elif(op == 2):
        bi = b
    elif(op == 3):
        ai = 0
    elif(op == 4):
        bi = 0
    elif(op == 5):
        if(b-bi>ai):
            bi = ai + bi
            ai = 0
        else:
            ai = ai - (b - bi)
            bi = b
    elif(op == 6):
        if(a-ai>bi):
            ai = ai + bi
            bi = 0
        else:
            bi = bi - (a- ai)
            ai = a
    elif(op == 7):
        ai = ai + bi
        bi = 0
    elif(op == 8):
        bi = bi + ai
        ai = 0
    print(ai, bi)

# 4. N Queens problem
n = int(input("Enter the value of n"))
board = []

def getBoard():
    for i in range(n):
        nthList = []
        for j in range(n):
            nthList.append(0)
        board.append(nthList)

def printBoard():
    for i in range(n):
        for j in range(n):
            print(board[i][j], end = " ")
        print("")
        
def isSafe(row, col):
    for i in range(n):
        if board[row][i] == 1:
            return False
    
    for j in range(n):
        if board[j][col] == 1:
            return False
     
    i = row-1
    j = col-1
    while(i>=0 and j>=0):
        if board[i][j] == 1:
            return False
        i = i-1
        j = j-1
       
    i = row-1
    j = col+1
    while(i>=0 and j<n):
        if board[i][j] == 1:
            return False
        i = i-1
        j = j+1
       
    i = row+1
    j = col-1
    while(i<n and j>=0):
        if board[i][j] == 1:
            return False
        i = i+1
        j = j-1
       
    i = row+1
    j = col+1
    while(i<n and j<n):
        if board[i][j] == 1:
            return False
        i = i+1
        j = j+1
    return True

def Put(n, count):
    if count == n:
        return True
    for i in range(n):
        for j in range(n):
            if isSafe(i, j):
                board[i][j] = 1
                count = count+1
                if Put(n, count) == True:
                    return True
                board[i][j] = 0
                count = count-1
    return False

getBoard()
Put(n, 0)
printBoard()
