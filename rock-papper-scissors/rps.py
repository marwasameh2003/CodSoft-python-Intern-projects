from tkinter import *
from tkinter import ttk
from random import randint
root= Tk()
root.title('Rock, Paper, Scissors')
root.geometry("500x600")

root.config(bg="white")

paper = PhotoImage(file='images/paper.png').subsample(1)  # Change 3 to your desired size factor
rock = PhotoImage(file='images/rock.png').subsample(3)
scissors = PhotoImage(file='images/scissor.png').subsample(-1)

image_list = [rock, paper, scissors]
pick_number = randint(0,2)
print(pick_number)
image_label = Label(root, image=image_list[pick_number])
image_label.pack(pady=20)

def spin():
    pick_number = randint(0,2)
    image_label.config(image=image_list[pick_number])
    
    if user_choice.get()=="Rock":
        user_choice_value = 0
    elif user_choice.get()=="Paper":
        user_choice_value = 1
    elif user_choice.get()=="Scissors":
        user_choice_value = 2

    if user_choice_value ==0:
        if pick_number == 0:
            win_lose_label.config(text="It's a Tie, spin again")
        elif pick_number == 1:
            win_lose_label.config(text="Paper covers rock, you lose :(")
        elif pick_number == 2:
            win_lose_label.config(text="Rock smashes scissors, you win :)")
            
    elif user_choice_value ==1:
        if pick_number == 0:
            win_lose_label.config(text="Paper covers rock, you win :)")
        elif pick_number == 1:
            win_lose_label.config(text="It's a Tie, spin again")
        elif pick_number == 2:
            win_lose_label.config(text="Scissors cut paper, you lose :(")

    elif user_choice_value ==2:
        if pick_number == 0:
            win_lose_label.config(text="Rock smashes scissors, you lose :(")
        elif pick_number == 1:
            win_lose_label.config(text="Scissors cut paper, you win :)")
        elif pick_number == 2:
            win_lose_label.config(text="It's a Tie, spin again")
user_choice = ttk.Combobox(root, values=("Rock", "Paper","Scissors"))
user_choice.current(0)
user_choice.pack(pady=20)
spin_button = Button(root, text="Spin!", command=spin)
spin_button.pack(pady=10)
win_lose_label = Label(root, text="",font=("Helvetica",18), bg="white")
win_lose_label.pack(pady=50)

root.mainloop()