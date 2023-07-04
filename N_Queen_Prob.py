from tkinter import *
from tkinter import messagebox
root=Tk()

def click1(): 
    #chessboard
    #NxN matrix with all elements 0
    N=int(e.get())
    board = [[0]*N for b in range(N)]
        
    def is_attack(i, j):
        #checking if there is a queen in row or column
        for k in range(0,N):
            if board[i][k]==1 or board[k][j]==1:
                return True
        #checking diagonals
        for k in range(0,N):
            for l in range(0,N):
                if (k+l==i+j) or (k-l==i-j):
                    if board[k][l]==1:
                        return True
        return False

    def N_queen(n):
        #if n is 0,solution is found (n represents no of queens left to be placed)
        if n==0:
            return True
        for i in range(N):
            for j in range(N):
                '''checking if we can place a queen here or not
                queen will not be placed if the place is being attacked
                or already occupied'''
                if (not(is_attack(i,j))) and (board[i][j]!=1):
                    board[i][j] = 1
                    #recursion
                    #wether we can put the next queen with this arrangment or not
                    if N_queen(n-1)==True:
                        return True
                    board[i][j] = 0
        return False

    N_queen(N)

    #Checking if solution is available or not
    count=0
    for i in range(N):
        for j in range(N):
            if board[i][j]==1:
                count=count+1

    if count!=N:
        messagebox.showerror("showerror", "No Solution Exists")
        ans=messagebox.askretrycancel("askretrycancel", "Try again?")
        if ans:
            e.delete(0,END)
        else:
            root.destroy()
    else:
        canvas=Canvas(root,width=1000,height=1000)
        color=True
        if N%2==0:
            for x in range(50,50*N+1,50):
                for y in range(50,50*N+1,50):
                    if color==True:
                        canvas.create_rectangle(x,y,x+50,y+50,fill="white")
                        if board[int(x/50)-1][int(y/50)-1]==1:
                            canvas.create_text(x+25,y+25,text="Q",fill="black",font="bold")
                    else:
                        canvas.create_rectangle(x,y,x+50,y+50,fill="black")
                        if board[int(x/50)-1][int(y/50)-1]==1:
                            canvas.create_text(x+25,y+25,text="Q",fill="white",font="bold")
                    color=not color
                color=not color
        else:
            for x in range(50,50*N+1,50):
                for y in range(50,50*N+1,50):
                    if color==True:
                        canvas.create_rectangle(x,y,x+50,y+50,fill="white")
                        if board[int(x/50)-1][int(y/50)-1]==1:
                            canvas.create_text(x+25,y+25,text="Q",fill="black",font="bold")
                    else:
                        canvas.create_rectangle(x,y,x+50,y+50,fill="black")
                        if board[int(x/50)-1][int(y/50)-1]==1:
                            canvas.create_text(x+25,y+25,text="Q",fill="white",font="bold")
                    color=not color
        canvas.pack()
        
        def a():
            ans=messagebox.askyesno("askyesno", "Try again?")
            if ans:
                canvas.destroy()
                e.delete(0,END)
            else:
                root.destroy()
        root.after(1000,a)
global canvas
l=Label(root,text='Enter the value of N')
l.pack()
global e
e=Entry(root)
e.pack()
b1=Button(root,text='click',command=click1)
b1.pack()
root.mainloop()
