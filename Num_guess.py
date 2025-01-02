import tkinter as tk
import random
import tkinter.messagebox as messagebox



def disable_input():
    guess_entry.config(state="disabled")
    guess_button.config(state="disabled")

def set_difficulty():
    global secret_num
    difficulty = difficulty_var.get()
    if difficulty=="easy":
        secret_num= random.randint(1,50)
    elif difficulty=="medium":
        secret_num= random.randint(1,100)
    else:
        secret_num= random.randint(1,1000)

#Main window
window = tk.Tk()
window.title("Number Guessing Game")


difficulty_var= tk.StringVar(value="medium")
tk.Label(window,text="Set difficulty: ").pack()
tk.Radiobutton(window,text="Easy (1-50)",variable=difficulty_var,value="easy",command=set_difficulty).pack()
tk.Radiobutton(window,text="Medium (1-100)",variable=difficulty_var,value="medium",command=set_difficulty).pack()
tk.Radiobutton(window,text="Hard (1-1000)",variable=difficulty_var,value="hard",command=set_difficulty).pack()

secret_num = 0
remaining_guess = 7
wins=0
losses=0

diff = difficulty_var.get()
if diff=="easy":
    secret_num=random.randint(1,50)
elif diff=="medium":
    secret_num= random.randint(1,100)
else:
    secret_num= random.randint(1,1000)


def check_guess():
    global remaining_guess,secret_num,difficulty_var,wins,losses
    try:
        guess = int(guess_entry.get())
        difficulty = difficulty_var.get()
        if (difficulty=="easy" and not 1<=guess<=50) or (difficulty=="medium" and not 1<=guess<=100) or (difficulty=="hard" and not 1<=guess<=1000):
            feedback_label.config(text="Guess out of range for the selected difficulty!")
            remaining_guess+=1
            return
        
        remaining_guess-=1
        guess_label.config(text=f"Guesses left : {remaining_guess}")

        if guess<secret_num:
            feedback_label.config(text="Higher!",bg="lightblue")
        elif guess>secret_num:
            feedback_label.config(text="Lower!",bg="lightpink")
        else:
            feedback_label.config(text="Correct! you guessed it!",bg="lightgreen")
            disable_input()
            wins+=1
            wins_label.config(text=f"Wins : {wins}")
            messagebox.showinfo("Congratulation!","You guessed the number!")

        if remaining_guess==0:
            feedback_label.config(text=f"You lose! The number was {secret_num}")
            disable_input()
            losses+=1
            losses_label.config(text=f"Losses : {losses}")

    except ValueError as e:
        #feedback_label.config(text="Invalid input. Please enter a number.")
        feedback_label.config(text=f"Invalid input: {e}")
    pass


def restart_game():
    global secret_num,remaining_guess,wins,losses
    set_difficulty()
    remaining_guess=7
    guess_label.config(text=f"Guess left : {remaining_guess}")
    feedback_label.config(text="",bg="SystemButtonFace")
    guess_entry.config(state="normal")
    guess_button.config(state="normal")
    guess_entry.delete(0,tk.END)


#Create an entry field for player's guess
guess_entry = tk.Entry(window)
guess_entry.pack()

#Guess button 
guess_button = tk.Button(window,text="Guess",command=check_guess)
guess_button.pack()
guess_entry.bind("<Return>",lambda event: check_guess())

#feedback message
feedback_label = tk.Label(window,text='')
feedback_label.pack()

#Creating a label to display remaining guesses
guess_label= tk.Label(window,text=f"Guesses left: {remaining_guess}")
guess_label.pack()

wins_label= tk.Label(window,text=f"Wins : {wins}")
wins_label.pack()

losses_label = tk.Label(window,text=f"Losses : {losses}")
losses_label.pack()

restart_button = tk.Button(window,text="Restart",command=restart_game)
restart_button.pack()


window.mainloop()