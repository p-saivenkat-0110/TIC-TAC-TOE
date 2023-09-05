import tkinter
from tkinter import messagebox
root=tkinter.Tk()
root.wm_state("zoomed")
sw=root.winfo_screenwidth()
sh=root.winfo_screenheight()
root.wm_minsize(sw,sh)
root.title("Tic-Tac-Toe")
root.configure(bg="#2b061b")
game=tkinter.Label(root,text="TIC-TAC-TOE",font=("Times New Roman",65),bg="#2b061b",fg="white",padx=100)
game.place(x=sw//2,y=10)

board=[["-" for _ in range(3)] for _ in range(3)]
wincolor="#0cb800"
tiecolor="#babd00"

def fillcolor(row=None,col=None):
    if row==0 and col==None:
        b1.config(bg=wincolor)
        b2.config(bg=wincolor)
        b3.config(bg=wincolor)
    elif row==1 and col==None:
        b4.config(bg=wincolor)
        b5.config(bg=wincolor)
        b6.config(bg=wincolor)
    elif row==2 and col==None:
        b7.config(bg=wincolor)
        b8.config(bg=wincolor)
        b9.config(bg=wincolor)
    elif row==None and col==0:
        b1.config(bg=wincolor)
        b4.config(bg=wincolor)
        b7.config(bg=wincolor)
    elif row==None and col==1:
        b2.config(bg=wincolor)
        b5.config(bg=wincolor)
        b8.config(bg=wincolor)
    elif row==None and col==2:
        b3.config(bg=wincolor)
        b6.config(bg=wincolor)
        b9.config(bg=wincolor)
    elif row==col:
        b1.config(bg=wincolor)
        b5.config(bg=wincolor)
        b9.config(bg=wincolor)
    else:
        b3.config(bg=wincolor)
        b5.config(bg=wincolor)
        b7.config(bg=wincolor)

def check(mat):
    if (mat[0][0]==mat[1][1]==mat[2][2]=="X"):
        fillcolor(0,0)
        return "X"
    
    if (mat[0][2]==mat[1][1]==mat[2][0]=="X"):
        fillcolor(0,2)
        return "X"
    
    if (mat[0][0]==mat[1][1]==mat[2][2]=="O"):
        fillcolor(0,0)
        return "O"
    
    if (mat[0][2]==mat[1][1]==mat[2][0]=="O"):
        fillcolor(0,2)
        return "O"
    
    for i in range(3):
        if (mat[i][0]==mat[i][1]==mat[i][2]=="X"):
            fillcolor(i,None)
            return "X"
        if (mat[0][i]==mat[1][i]==mat[2][i]=="X"):
            fillcolor(None,i)
            return "X"
        if (mat[i][0]==mat[i][1]==mat[i][2]=="O"):
            fillcolor(i,None)
            return "O"
        if (mat[0][i]==mat[1][i]==mat[2][i]=="O"):
            fillcolor(None,i)
            return "O"
        
    dash=0
    for i in range(3):
        if "-" in mat[i]:
            dash=1
            break
    if dash:
        return "Pending"
    else:
        return "Tie"


def stop(color=None):
    b1.config(state="disabled")
    b2.config(state="disabled")
    b3.config(state="disabled")
    b4.config(state="disabled")
    b5.config(state="disabled")
    b6.config(state="disabled")
    b7.config(state="disabled")
    b8.config(state="disabled")
    b9.config(state="disabled")
    if color:
        b1.config(bg=tiecolor)
        b2.config(bg=tiecolor)
        b3.config(bg=tiecolor)
        b4.config(bg=tiecolor)
        b5.config(bg=tiecolor)
        b6.config(bg=tiecolor)
        b7.config(bg=tiecolor)
        b8.config(bg=tiecolor)
        b9.config(bg=tiecolor)

turn="❌"
def play(t=None):
    global turn
    if turn=="❌":
        fill="X"
        turnL.config(text="'O' Turn")
        turnshow.config(text=pat2)
    else:
        fill="O"
        turnL.config(text="'X' Turn")
        turnshow.config(text=pat1)
        
    if t=="b1":
        b1.configure(text=turn,state="disabled")
        board[0][0]=fill
    elif t=="b2":
        b2.configure(text=turn,state="disabled")
        board[0][1]=fill
    elif t=="b3":
        b3.configure(text=turn,state="disabled")
        board[0][2]=fill
    elif t=="b4":
        b4.configure(text=turn,state="disabled")
        board[1][0]=fill
    elif t=="b5":
        b5.configure(text=turn,state="disabled")
        board[1][1]=fill
    elif t=="b6":
        b6.configure(text=turn,state="disabled")
        board[1][2]=fill
    elif t=="b7":
        b7.configure(text=turn,state="disabled")
        board[2][0]=fill
    elif t=="b8":
        b8.configure(text=turn,state="disabled")
        board[2][1]=fill
    else:
        b9.configure(text=turn,state="disabled")
        board[2][2]=fill
        
    decision = check(board)
    if decision!="Pending":
        turnL.config(text="  --------")
        turnshow.config(text="")
        if decision=="Tie":
            stop(tiecolor)
            messagebox.showinfo("VICTORY"," OH NO!!, TIE Match😐 ")
        else:
            stop()
            messagebox.showinfo("VICTORY",f" 🎉Congratulations🎉, '{decision}' WON the match...")
        startB.config(text="Restart",state="active")
        reset["state"]="disabled"   
        
    if turn=="❌":
        turn="⭕"
    else:
        turn="❌"
    
gridFrame=tkinter.Frame(root)
gw=33
gh=13
b1=tkinter.Button(gridFrame,width=gw,height=gh,state="disabled",command=lambda: play("b1"))
b1.grid(row=0,column=0)
b2=tkinter.Button(gridFrame,width=gw,height=gh,state="disabled",command=lambda: play("b2"))
b2.grid(row=0,column=1)
b3=tkinter.Button(gridFrame,width=gw,height=gh,state="disabled",command=lambda: play("b3"))
b3.grid(row=0,column=2)
b4=tkinter.Button(gridFrame,width=gw,height=gh,state="disabled",command=lambda: play("b4"))
b4.grid(row=1,column=0)
b5=tkinter.Button(gridFrame,width=gw,height=gh,state="disabled",command=lambda: play("b5"))
b5.grid(row=1,column=1)
b6=tkinter.Button(gridFrame,width=gw,height=gh,state="disabled",command=lambda: play("b6"))
b6.grid(row=1,column=2)
b7=tkinter.Button(gridFrame,width=gw,height=gh,state="disabled",command=lambda: play("b7"))
b7.grid(row=2,column=0)
b8=tkinter.Button(gridFrame,width=gw,height=gh,state="disabled",command=lambda: play("b8"))
b8.grid(row=2,column=1)
b9=tkinter.Button(gridFrame,width=gw,height=gh,state="disabled",command=lambda: play("b9"))
b9.grid(row=2,column=2)
gridFrame.pack(side="left",padx=50)


player1_img=tkinter.PhotoImage(file="player.png")
player1=tkinter.Label(root,image=player1_img)
player1.place(x=(sw//2)+95,y=sh//5)
player2=tkinter.Label(root,image=player1_img)
player2.place(x=(sw//2)+425,y=sh//5)

p1_Label=tkinter.Label(root,text="Player 1",font=("Calibri",18),bg="#2b061b",fg="white")
p2_Label=tkinter.Label(root,text="Player 2",font=("Calibri",18),bg="#2b061b",fg="white")
p1_Label.place(x=(sw//2)+165,y=(sh//6)-8)
p2_Label.place(x=(sw//2)+500,y=(sh//6)-8)

pn1=tkinter.Label(root,text="TIC\n(Your coin is 'X')",justify="center",width=19,font=("",15),bg="#2b061b",fg="yellow")
pn1.place(x=(sw//2)+96,y=(sh//2)-28)
pn2=tkinter.Label(root,text="TOE\n(Your coin is 'O')",justify="center",width=19,font=("",15),bg="#2b061b",fg="yellow")
pn2.place(x=(sw//2)+426,y=(sh//2)-28)

def clearBoard():
    global turn
    turnL.config(text="'X' Turn")
    turnshow.config(text=pat1)
    turn="❌"
    b1.config(text="",bg="white",state="active")
    b2.config(text="",bg="white",state="active")
    b3.config(text="",bg="white",state="active")
    b4.config(text="",bg="white",state="active")
    b5.config(text="",bg="white",state="active")
    b6.config(text="",bg="white",state="active")
    b7.config(text="",bg="white",state="active")
    b8.config(text="",bg="white",state="active")
    b9.config(text="",bg="white",state="active")
    for i in range(3):
        for j in range(3):
            board[i][j]="-"
    
def start():
    startB["state"]="disabled"
    reset["state"]="active"
    clearBoard()

pat1="👈\n👈\n👈\n👈\n👈\n👈\n👈\n👈\n👈\n👈"
pat2="👉\n👉\n👉\n👉\n👉\n👉\n👉\n👉\n👉\n👉"
turnshow=tkinter.Label(root,bg="#2b061b",fg="orange",font=("",20))
turnshow.place(x=(sw//2)+355,y=(sh//7)+5)

turnL=tkinter.Label(root,text="  --------",font=("",55),bg="#2b061b",fg="orange")
turnL.place(x=(sw//2)+250,y=(sh//2)+40)

startB=tkinter.Button(root,text="Start",font=("",16),width=20,command=start)
startB.place(x=(sw//2)+265,y=(sh//2)+140)

reset=tkinter.Button(root,text="Reset Board",font=("",16),state="disabled",width=20,command=clearBoard)
reset.place(x=(sw//2)+265,y=(sh//2)+200)

quit=tkinter.Button(root,text="Quit",font=("",16),width=20,command=exit)
quit.place(x=(sw//2)+265,y=(sh//2)+260)

root.mainloop()
