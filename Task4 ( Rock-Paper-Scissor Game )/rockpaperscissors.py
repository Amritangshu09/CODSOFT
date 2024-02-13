from tkinter import *
from PIL import Image, ImageTk
from random import randint

window = Tk()
#window.geometry('900x350')
#window.resizable(width=True,height=True)
window.title("Rock-Paper-Scissors")
window.configure(background="Sky blue")

image_rock1 = ImageTk.PhotoImage((Image.open("rock hand computer.png")).resize((100,100)))
image_paper1 = ImageTk.PhotoImage((Image.open("paper hand2.png")).resize((100,100)))
image_scissor1 = ImageTk.PhotoImage((Image.open("scissors hand.png")).resize((100,100)))
image_rock2 = ImageTk.PhotoImage((Image.open("rock hand.png")).resize((100,100)))
image_paper2 = ImageTk.PhotoImage((Image.open("paper hand computer.png")).resize((100,100)))
image_scissor2 = ImageTk.PhotoImage((Image.open("scissors hand computer.png")).resize((100,100)))

label_player = Label(window,image=image_scissor1,bg="sky blue")
label_computer = Label(window,image=image_scissor2,bg="sky blue")
label_computer.grid(row=1,column=0)
label_player.grid(row=1,column=4)

computer_score= Label(window,text=0,font=('arial',60,'bold'),bg="sky blue",fg="green")
player_score= Label(window,text=0,font=('arial',60,'bold'),bg="skyblue",fg="green")
player_score.grid(row=1,column=3)
computer_score.grid(row=1,column=1)

player_indi =  Label(window,font=("Britannic Bold",40,"bold"),text="PLAYER",bg="sky blue",fg="orange")
computer_indi =  Label(window,font=("Britannic Bold",40,"bold"),text="COMPUTER",bg="sky blue",fg="orange")
computer_indi.grid(row=0,column=1)
player_indi.grid(row=0,column=3)

def updateMessage(a):
    final_message['text'] = a

def computer_update():
    final = int (computer_score['text'])
    final+=1
    computer_score["text"]=str(final)
    if final == 10:
        updateMessage("Computer Wins the Game!")


def player_update():
    final = int (player_score['text'])
    final+=1
    player_score["text"]=str(final)
    if final == 10:
        updateMessage("Player Wins the Game!")

    
def winner_check(p,c):
    if p == c:
        updateMessage("It's a Tie")
    elif p == "rock":
        if c == "paper":
            updateMessage("Computer Wins!!")
            computer_update()
        else:
            updateMessage("Player Wins!!")
            player_update()
    elif p == "paper":
        if c == "scissor":
            updateMessage("Computer Wins!!")
            computer_update()
        else:
            updateMessage("Player Wins!!")
            player_update()
    elif p == "scissor":
        if c == "rock":
            updateMessage("Computer Wins!!")
            computer_update()
        else:
            updateMessage("Player Wins!!")
            player_update()
    else:
        pass

to_select=["rock","paper","scissor"]

def choice_update(a):
    choice_computer=to_select[randint(0,2)]
    if choice_computer == "rock":
        label_computer.configure(image=image_rock2)
    elif choice_computer == "paper":
        label_computer.configure(image=image_paper2)
    else: 
        label_computer.configure(image=image_scissor2)
    if a =="rock":
        label_player.configure(image=image_rock1)
    elif a == "paper":
        label_player.configure(image=image_paper1)
    else:
        label_player.configure(image=image_scissor1)
    
    winner_check(a,choice_computer)


final_message =  Label(window,font=("Cascadia Mono",30,"bold"),bg="sky blue",fg="indigo")
final_message.grid(row=3,column=2)

button_rock = Button(window,width=8,height=2,text="ROCK",font=("Arial",20,"bold"),bg="Yellow",fg="red",padx=5,pady=5,activebackground="brown",activeforeground="yellow",highlightthickness=2,highlightcolor="white",highlightbackground="green",cursor="hand1",command= lambda:choice_update("rock")).grid(row=2,column=1)
button_paper = Button(window,width=8,height=2,text="PAPER",font=("Arial",20,"bold"),bg="brown",fg="Yellow",padx=5,pady=5,activebackground="yellow",activeforeground="red",highlightthickness=2,highlightcolor="white",highlightbackground="green",cursor="hand1",command= lambda:choice_update("paper")).grid(row=2,column=2)
button_scissor = Button(window,width=8,height=2,text="SCISSOR",font=("Arial",20,"bold"),bg="Yellow",fg="red",padx=5,pady=5,activebackground="brown",activeforeground="yellow",highlightthickness=2,highlightcolor="white",highlightbackground="green",cursor="hand1",command= lambda:choice_update("scissor")).grid(row=2,column=3)



window.mainloop()
