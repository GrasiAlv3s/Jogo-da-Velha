import random

board = [ "-", "-", "-",
          "-", "-", "-",
          "-", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True

#Tabuleiro de jogo

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

#Receber a opinião do jogador

def playerImput (board):
    inp = int(input("Escolha entre 1-9: "))
    if board [inp-1] == "-":
        board [inp-1] = currentPlayer
    else:
        print ("Opps, escolha novamente")

#Verificar se há vitória ou empate
def checkHorizontle(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
    
def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[3]
        return True

def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "-":
        winner = board[2]
        return True
    
def checkIfWin(board):
    global gameRunning
    if checkHorizontle(board):
        printBoard(board)
        print(f"O ganhador é {winner}")
        gameRunning = False

    elif checkRow(board):
        printBoard(board)
        print(f"O ganhador é{winner}!")
        gameRunning = False

    elif checkDiag(board):
        printBoard(board)
        print(f"O ganhador é {winner}!")
        gameRunning = False

def checkIfTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("Deu velha :(")
        gameRunning = False

#Trocar de Jogador
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

def computer(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()


while gameRunning:
    printBoard(board)
    playerImput(board)
    checkIfWin(board)
    checkIfTie(board)
    switchPlayer()
    computer(board)
    checkIfWin(board)
    checkIfTie(board)



git remote add origin https://github.com/GrasiAlv3s/Jogo-da-Velha02.git
 git branch -M main 
git push -u origin main