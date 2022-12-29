import random



def start():
    player = ""
    computer = ""
    print("Welcome to Tic Tac Toe!\n")
    print("The player will have to select 'X' or 'O' and take turns filling a 3x3 grid.\n")
    print("The player will compete against a computer\n")
    print("The first to get 3 of the marks in a row either vertical, horizonal or diagonal wins!\n")

    while True:
        player = input("Player, do you wish to be X or O?")
        if player == "X":
            computer = "O"
            print("Okay, Computer will be O")
            break
        elif player == "O":
            computer = "X"
            print("Okay, Computer will be X")
            break
        else:
            print("You can only input either X or O!")
    return(player, computer)



def makeGrid():
    print("Here is the playboard")
    board = [[" ", " ", " ",], 
            [" ", " ", " "], 
            [" ", " ", " "]]
    return board

def game(board, player, computer, count):
    if count % 2 == 0:
        playerTurn = True
        while playerTurn == True:
            print ("It is the turn of the player")
            row = int(input("Pick a row coord"))
            col = int(input("Pick a collumn coord"))
            
            while (row > 2 or row < 0) or (col > 2 or col < 0):
                print("Please select a valid coord\n")
                print ("It is the turn of the player")
                row = int(input("Pick a row coord"))
                col = int(input("Pick a collumn coord"))
            
            while (board[row][col] == player) or (board[row][col] == computer):
                print("An illegal move has been made")
                print ("It is the turn of the player")
                row = int(input("Pick a row coord"))
                col = int(input("Pick a collumn coord"))
            
            board[row][col] = player
            playerTurn = False    
    elif count % 2 == 1:
        playerTurn = False
        print ("It is the turn of the computer")
        while playerTurn == False:
            comprow = random.randint(0,2)
            compcol = random.randint(0,2)
            while (comprow > 2 or comprow < 0) or (compcol > 2 or compcol < 0):
                print("Computer picked an invalid coord, silly computer!\n")
                print ("It is the turn of the Computer")
                comprow = random.randint(0,2)
                compcol = random.randint(0,2)
            while (board[comprow][compcol] == player) or (board[comprow][compcol] == computer):
                print("An illegal move has been made")
                print ("It is the turn of the computer")
                comprow = random.randint(0,2)
                compcol = random.randint(0,2)
            board[comprow][compcol] = computer
            playerTurn = True       
    return (board)
        
    
def display(board):
    rowlen = len(board)
    collen = len(board)
    print ("---+---+---")
    for i in range(rowlen):
        print(board[i][0], " |", board[i][1],"|", board[i][2])
        print("---+---+---")
    return board


def full(board, player, computer):
    count = 0
    win = False
    while count <9 and win == False:
        play = game(board, player, computer, count)
        displayBoard = display(board)

        if count == 8:
            print("The board is full.")
            if win == False:
                print("Stalemate.")
        win = winCon(board, player, computer)
        count += 1
    if win == True:
        print("Game over")
        
    print("\n")
    input("Press Enter to see the game report!")
    if (win == True) and (count%2 == 1):
        print("Player is the winner")
    elif (win == True) and (count %2 == 0):
        print("Computer is winner")
    else:
        print("game is a tie!")

def winCon(board, player, computer):
    win = False
    #rows
    for row in range (0, 3):
        if (board[row][0] == board[row][1] == board[row][2] == player):
            win = True
            print("Player wins")
        elif (board[row][0] == board[row][1] == board[row][2] == computer):
            win = True
            print ("Computer wins")
    #cols
    for col in range (0,3):
        if (board[0][col] == board[1][col] == board[2][col] == player):
            win = True
            print("Player wins")
        elif(board[0][col] == board[1][col] == board[2][col] == computer):
            win = True
            print("Computer wins")
    
    #diags
    if (board[0][0] == board[1][1] == board[2][2] == player):
        win = True
        print("Player wins")
    elif (board[0][0] == board[1][1] == board[2][2] == computer) :
        win = True
        print("Computer wins")
    elif (board [0][2] == board [1][1] == board [2][0] == player):
        win = True
        print("Player wins")
    elif (board [0][2] == board [1][1] == board [2][0] == computer):
        win = True
        print("Computer wins")
    return win

def main():
    player, computer = start()
    print (player)
    p = print("Creating a board!")
    print (player)
    g = makeGrid()
    print (player)
    d = display(g)
    f = full(g, player, computer)

if __name__ == "__main__":
    main()