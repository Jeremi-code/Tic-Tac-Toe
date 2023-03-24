import random

board=["-","-","-","-","-","-","-","-","-",]
currentPlayer="X"
winner=None
gameRunning=True 

def printBoard(board):
    print(board[0]+    "|"   + board[1]    + "|" + board[2])
    print("-----")
    print(board[3]+    "|"   + board[4]    + "|" + board[5])
    print("-----")
    print(board[6]+    "|"   + board[7]    + "|" + board[8])
    print("-----")
def playerInput(board):
    inp=int(input("enter a number 1-9: "))
    if inp >=1 and inp<=9 and board[inp-1]=='-':
        board[inp-1]=currentPlayer
    elif board[inp-1]=='-' :
        print("Oops player is already in that spot")
    else :
        print("You have chosen an already spotted place")
        playerInput(board)


def checkHorizontle(board):
    global winner 
    if board[0] == board[1] == board[2] and board[1]!= "-":
        winner=board[0]
        return True
    elif board[3] == board[4] == board [5] and board[3]!="-":
        winner=board[3]
        return True 
    elif board[6] == board[7] == board[8] and board[7]!= "-":
        winner= board[2]
        return True 
def checkVerticale(board):
    global winner
    if board[0] == board[3] == board[6] and board[3]!="-":
        winner =board[3]
        return True
    elif  board[1] == board[4] == board[7] and board[4]!="-":
        winner =board[3]
        return True
    elif board[2] == board[5] == board[8] and board[5]!="-":
        winner =board[3]
        return True
    
def checkDiag(board):
    global winner 
    if board[0] == board [4] == board[8] and board[0]!="-":
        winner=board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2]!="-":
        winner=board[2]
        return True 
def checkTie(board):
    global gameRunning
    if "-" not in board :
        printBoard(board)
        print("It is a tie")
        gameRunning=False
def checkWin():
    global gameRunning
    global winner
    if checkDiag(board)==True or checkHorizontle( board)==True or checkVerticale(board) == True :
        print ( "The winner of this match is " + winner )
        gameRunning=False
def computer(board):
    while currentPlayer == "O":
        position=random.randint(0,8)
        if board[position]=="-":
            board[position]="0"
            switchPlayer()
        else:
            computer(board)
       

def switchPlayer():
    global currentPlayer
    if currentPlayer=="X":
        currentPlayer="O"
    else:
        currentPlayer="X"
print("1. Computer")
print("2. Friend")
inpu=int(input("Do you want to play with your friend or a computer "))

if inpu==1:
    while gameRunning:

        printBoard(board)
        playerInput(board)
        checkWin()
        checkTie(board)
        switchPlayer()
        computer(board)
        checkWin()
        checkTie(board)
elif inpu==2:
    while gameRunning:
        printBoard(board)
        playerInput(board)
        checkWin()
        checkTie(board)
        switchPlayer()
   


