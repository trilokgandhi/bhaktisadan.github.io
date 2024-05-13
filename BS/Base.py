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

#5 Write a program to implement Tower of Hanoi Problem.


# Recursive Python function to solve the tower of hanoi

def TowerOfHanoi(n , source, destination, auxiliary):
	if n==1:
		print ("Move disk 1 from source",source,"to destination",destination)
		return
	TowerOfHanoi(n-1, source, auxiliary, destination)
	print ("Move disk",n,"from source",source,"to destination",destination)
	TowerOfHanoi(n-1, auxiliary, destination, source)
		
n = 4
TowerOfHanoi(n,'A','B','C') 

#6: Write a prolog program for the family tree.


parent(pam,bob).
parent(tom,bob).
parent(tom,liz).
parent(bob,ann).
parent(bob,pat).
parent(pat,jim).

female(pam).
male(tom).
male(bob).
female(liz).
female(pat).
female(ann).
male(jim).

grandparent(GP, GC) :-
    parent(GP, Parent),
    parent(Parent, GC).

sibling(X, Y) :-
    parent(P, X),
    parent(P, Y),
    X\=Y.

brother(X, Y) :-
    male(X),
    sibling(X, Y).

sister(X, Y) :-
    female(X),
    sibling(X, Y).

uncle(X, Z) :-
    brother(X, Y),
    parent(Y, Z).

aunt(X, Z) :-
    sister(X, Y),
    parent(Y, Z).

#7 Write a program to solve N-Queens problem using Prolog.


n_queens(N, Solution) :-
	%create a list of N dummy variabiles
	length(Solution, N),

	queen(Solution, N). %search for a configuration of N queens


%returns a list of integer from K to N included es up2N(1,3,X) X = [1,2,3]
up2N(N,N,[N]) :-!.
up2N(K,N,[K|Tail]) :- K < N, K1 is K+1, up2N(K1, N, Tail).


queen([],_). %No queens is a solution for any N queens problem. All queens are in a safe position.

queen([Q|Qlist],N) :-

	queen(Qlist, N), %first we solve the subproblem

	%we then generate all possible positions for queen Q
	up2N(1,N,Candidate_positions_for_queenQ),

	%we pick one of such position
	member(Q, Candidate_positions_for_queenQ),

	%we check whether the queen Q is safe
	check_solution(Q,Qlist, 1).



check_solution(_,[], _).

check_solution(Q,[Q1|Qlist],Xdist) :-
	Q =\= Q1, %not on the same row
	Test is abs(Q1-Q),
	Test =\= Xdist, %diagonal distance
	Xdist1 is Xdist + 1,
	check_solution(Q,Qlist,Xdist1).
    
#8:  Write a program to solve 8 puzzle problem using Prolog.


test(Plan):-
    write('Initial state:'),nl,
    Init= [at(tile4,1), at(tile3,2), at(tile8,3), at(empty,4), at(tile2,5), at(tile6,6), at(tile5,7), at(tile1,8), at(tile7,9)],
    write_sol(Init),
    Goal= [at(tile1,1), at(tile2,2), at(tile3,3), at(tile4,4), at(empty,5), at(tile5,6), at(tile6,7), at(tile7,8), at(tile8,9)],
    nl,write('Goal state:'),nl,
    write(Goal),nl,nl,
    solve(Init,Goal,Plan).

solve(State, Goal, Plan):-
    solve(State, Goal, [], Plan).

%Determines whether Current and Destination tiles are a valid move.
is_movable(X1,Y1) :- (1 is X1 - Y1) ; (-1 is X1 - Y1) ; (3 is X1 - Y1) ; (-3 is X1 - Y1).


% This predicate produces the plan. Once the Goal list is a subset
% of the current State the plan is complete and it is written to
% the screen using write_sol/1.

solve(State, Goal, Plan, Plan):-
    is_subset(Goal, State), nl,
    write_sol(Plan).

solve(State, Goal, Sofar, Plan):-
    act(Action, Preconditions, Delete, Add),
    is_subset(Preconditions, State),
    \+ member(Action, Sofar),
    delete_list(Delete, State, Remainder),
    append(Add, Remainder, NewState),
    solve(NewState, Goal, [Action|Sofar], Plan).

% The problem has three operators.
% 1st arg = name
% 2nd arg = preconditions
% 3rd arg = delete list
% 4th arg = add list.

% Tile can move to new position only if the destination tile is empty & Manhattan distance = 1
act(move(X,Y,Z),
    [at(X,Y), at(empty,Z), is_movable(Y,Z)],
    [at(X,Y), at(empty,Z)],
    [at(X,Z), at(empty,Y)]).


% Utility predicates.

% Check is first list is a subset of the second

is_subset([H|T], Set):-
    member(H, Set),
    is_subset(T, Set).
is_subset([], _).

% Remove all elements of 1st list from second to create third.

delete_list([H|T], Curstate, Newstate):-
    remove(H, Curstate, Remainder),
    delete_list(T, Remainder, Newstate).
delete_list([], Curstate, Curstate).

remove(X, [X|T], T).
remove(X, [H|T], [H|R]):-
    remove(X, T, R).

write_sol([]).
write_sol([H|T]):-
    write_sol(T),
    write(H), nl.

append([H|T], L1, [H|L2]):-
    append(T, L1, L2).
append([], L, L).

member(X, [X|_]).
member(X, [_|T]):-
    member(X, T).
