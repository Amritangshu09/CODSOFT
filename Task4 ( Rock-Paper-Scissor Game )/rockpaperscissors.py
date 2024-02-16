from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from random import randint

def set_game_mode():
    global match_points
    match_points = int(entry_match_points.get())
    if match_points != 5 and match_points != 10:
        messagebox.showwarning("Warning", "Please enter either 5 or 10 as match points!")
    else:
        messagebox.showinfo("Game Mode Selected", f"Match will be played up to {match_points} points.")
        reset_scores()

def reset_scores():
    player_score.config(text="0")
    computer_score.config(text="0")

def ask_continue():
    result = messagebox.askyesno("Continue Game", "Do you want to continue playing?")
    if result:
        reset_scores()
    else:
        window.destroy()

def updateMessage(a):
    final_message['text'] = a

def computer_update():
    final = int(computer_score['text']) + 1
    computer_score["text"] = str(final)
    if final == match_points:
        updateMessage("Computer Wins the Game!")
        ask_continue()

def player_update():
    final = int(player_score['text']) + 1
    player_score["text"] = str(final)
    if final == match_points:
        updateMessage("Player Wins the Game!")
        ask_continue()

def winner_check(p, c):
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

def choice_update(a):
    choice_computer = to_select[randint(0, 2)]
    if choice_computer == "rock":
        label_computer.configure(image=image_rock2)
    elif choice_computer == "paper":
        label_computer.configure(image=image_paper2)
    else:
        label_computer.configure(image=image_scissor2)
    if a == "rock":
        label_player.configure(image=image_rock1)
    elif a == "paper":
        label_player.configure(image=image_paper1)
    else:
        label_player.configure(image=image_scissor1)
    winner_check(a, choice_computer)

window = Tk()
window.title("Rock-Paper-Scissors")
window.configure(background="Sky blue")

# Load images
image_rock1 = ImageTk.PhotoImage((Image.open("rock hand computer.png")).resize((100, 100)))
image_paper1 = ImageTk.PhotoImage((Image.open("paper hand2.png")).resize((100, 100)))
image_scissor1 = ImageTk.PhotoImage((Image.open("scissors hand.png")).resize((100, 100)))
image_rock2 = ImageTk.PhotoImage((Image.open("rock hand.png")).resize((100, 100)))
image_paper2 = ImageTk.PhotoImage((Image.open("paper hand computer.png")).resize((100, 100)))
image_scissor2 = ImageTk.PhotoImage((Image.open("scissors hand computer.png")).resize((100, 100)))

# Player and computer labels
label_player = Label(window, image=image_scissor1, bg="sky blue")
label_computer = Label(window, image=image_scissor2, bg="sky blue")
label_computer.grid(row=1, column=0)
label_player.grid(row=1, column=4)

# Player and computer scores
computer_score = Label(window, text="0", font=('arial', 60, 'bold'), bg="sky blue", fg="green")
player_score = Label(window, text="0", font=('arial', 60, 'bold'), bg="sky blue", fg="green")
player_score.grid(row=1, column=3)
computer_score.grid(row=1, column=1)

# Player and computer indicators
player_indi = Label(window, font=("Britannic Bold", 40, "bold"), text="PLAYER", bg="sky blue", fg="orange")
computer_indi = Label(window, font=("Britannic Bold", 40, "bold"), text="COMPUTER", bg="sky blue", fg="orange")
computer_indi.grid(row=0, column=1)
player_indi.grid(row=0, column=3)

# Final message label
final_message = Label(window, font=("Cascadia Mono", 30, "bold"), bg="sky blue", fg="indigo")
final_message.grid(row=3, column=2)

# Buttons for user choice
button_rock = Button(window, width=8, height=2, text="ROCK", font=("Arial", 20, "bold"), bg="Yellow", fg="red",
                     padx=5, pady=5, activebackground="brown", activeforeground="yellow", highlightthickness=2,
                     highlightcolor="white", highlightbackground="green", cursor="hand1", command=lambda: choice_update("rock")).grid(row=2, column=1)
button_paper = Button(window, width=8, height=2, text="PAPER", font=("Arial", 20, "bold"), bg="brown", fg="Yellow",
                      padx=5, pady=5, activebackground="yellow", activeforeground="red", highlightthickness=2,
                      highlightcolor="white", highlightbackground="green", cursor="hand1", command=lambda: choice_update("paper")).grid(row=2, column=2)
button_scissor = Button(window, width=8, height=2, text="SCISSOR", font=("Arial", 20, "bold"), bg="Yellow", fg="red",
                        padx=5, pady=5, activebackground="brown", activeforeground="yellow", highlightthickness=2,
                        highlightcolor="white", highlightbackground="green", cursor="hand1", command=lambda: choice_update("scissor")).grid(row=2, column=3)

# Ask for game mode
label_match_points = Label(window, text="Enter Match Points (5 or 10):", font=("Arial", 12), bg="sky blue")
label_match_points.grid(row=4, column=0, padx=5, pady=5)
entry_match_points = Entry(window, font=("Arial", 12), width=10)
entry_match_points.grid(row=4, column=1, padx=5, pady=5)
button_start_game = Button(window, text="Start Game", font=("Arial", 12), command=set_game_mode)
button_start_game.grid(row=4, column=2, padx=5, pady=5)

to_select = ["rock", "paper", "scissor"]
match_points = 0  # Placeholder for match points

window.mainloop()
