import numpy as np
import tkinter as tk
from tkinter import messagebox

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

root=tk.Tk()
root.title("Tic Tac Toe - Human vs AI")
buttons=[[None for _ in range(3)] for _ in range(3)]

def update_buttons():
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=board[i][j])

def disable_buttons():
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(state=tk.DISABLED)

def enable_buttons():
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(state=tk.NORMAL)

def reset_game():
    for i in range(3):
        for j in range(3):
            board[i][j]=''
    update_buttons()
    enable_buttons()

def on_click(i,j):
    if board[i][j]=='':
        board[i][j]='X'
        update_buttons()

        result=check_winner(board)
        if result!=None:
            messagebox.showinfo("Game Over",f"{result} won!")
            disable_buttons()
            return
        elif isfull(board):
            messagebox.showinfo("Game Over","it's a draw")
            disable_buttons()
            return

        move=bestmove(board)
        if move!=None:
            a,b=move
            board[a][b]='O'
            update_buttons()

            result=check_winner(board)
            if result!=None:
                messagebox.showinfo("Game Over",f"{result} won!")
                disable_buttons()
            elif isfull(board):
                messagebox.showinfo("Game Over","it's a draw")
                disable_buttons()

for i in range(3):
    for j in range(3):
        button=tk.Button(root,text='',font=('Helvetica',20),width=5,height=2,command=lambda i=i,j=j: on_click(i,j))
        button.grid(row=i,column=j)
        buttons[i][j]=button

play_again_btn=tk.Button(root,text='Play Again',font=('Helvetica',14),command=reset_game)
play_again_btn.grid(row=3,column=0,columnspan=3,pady=10)

root.mainloop()