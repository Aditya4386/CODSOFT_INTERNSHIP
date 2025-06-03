import numpy as np


def check_winner(board):
    winner=None
    for i in range(3):

        if board[i][0]!='' and board[i][0]==board[i][1]==board[i][2]:
            winner=board[i][0]

        if board[0][i]!='' and board[0][i]==board[1][i]==board[2][i]:
            winner=board[0][i]

    if board[1][1]!='' and board[0][0]==board[1][1]==board[2][2]:
        winner=board[1][1]
    
    if board[1][1]!='' and board[0][2]==board[1][1]==board[2][0]:
        winner=board[1][1]

    return winner
    
        

def isfull(board):
    for i in range(3):
        for j in range(3):
            if board[i][j]=='':
                return False
    return True

def display(board):
    for i in range(3):
        print(f" {board[i][0]}  |  {board[i][1]}  |  {board[i][2]} ")
        if i<2:
            print("---+----+---")

def minimax(board,maximizing):
    winner=check_winner(board)
    if winner=='X':
        return -1
    
    if winner=='O':
        return 1
    
    if isfull(board):
        return 0
    
    if maximizing:
        bestscore=-9999
        for i in range(3):
            for j in range(3):
                if board[i][j]=='':
                    board[i][j]='O'
                    score=minimax(board,False)
                    board[i][j]=''
                    bestscore=max(score,bestscore)
        return bestscore
    else:
        bestscore=9999
        for i in range(3):
            for j in range(3):
                if board[i][j]=='':
                    board[i][j]='X'
                    score=minimax(board,True)
                    board[i][j]=''
                    bestscore=min(score,bestscore)
        return bestscore
    
def bestmove(board):
    bestscore=-9999
    move=None
    for i in range(3):
        for j in range(3):
            if board[i][j]=='':
                board[i][j]='O'
                score=minimax(board,False)
                board[i][j]=''
                if score>bestscore:
                    bestscore=score
                    move=(i,j)

    return move

board=[
    ['','',''],
    ['','',''],
    ['','','']
]
display(board)

while True:
    print("player 'X' move")
    print("Enter the row and column to specify the position")
    a=int(input())
    b=int(input())

    if a not in [0,1,2] or b not in [0,1,2]:
        print("enter the valid input")
        continue

    if board[a][b] != '':
        print("feild is not empty")
        continue 

    board[a][b]='X' 

    result=check_winner(board)
    if result!=None:
       print(result," Won")
       display(board)
       break

    display(board)

    if isfull(board):
        print("its a draw")
        break

    print("AI move")

    (a,b)=bestmove(board)
    board[a][b]='O'

    result=check_winner(board)
    if result!=None:
       print(result," Won")
       display(board)
       break
    
    display(board)

    if isfull(board):
        print("its a draw")
        break
