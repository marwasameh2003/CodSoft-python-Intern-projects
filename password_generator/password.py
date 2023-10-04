from tkinter import *
from tkinter import messagebox
from random import randint
from tkinter import ttk

# Define the color palette
bg_color = "#004225"  # Dark green
fg_color = "#F5F5DC"  # Beige
button_color = "#EFD595"  # Orange
entry_bg_color = "#FFCF9D"  # Light orange

def new_rand():
    pw_entry.delete(0, END)
    pw_length = int(my_entry.get())
    complexity = complexity_combo.get()
    
    if complexity == "Easy":
        charset = range(48, 58)  # Numeric characters
    elif complexity == "Intermediate":
        charset = range(33, 91)  # Alphanumeric characters and symbols
    else:
        charset = range(33, 127)  # All printable ASCII characters
    
    my_pass = ''.join(chr(randint(min(charset), max(charset))) for _ in range(pw_length))
    pw_entry.insert(0, my_pass)


def clipper():
    password = pw_entry.get()
    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()  # Required to trigger the clipboard update
    messagebox.showinfo("Success", "Password copied to clipboard!")

root = Tk()
root.title('Strong Password Generator')
root.geometry("500x450")

# Set background color for the root window
root.configure(bg=bg_color)

lf = LabelFrame(root, text="How Many Characters?", bg=bg_color, fg=fg_color)
lf.pack(pady=20)

my_entry = Entry(lf, font=("Helvetica", 24), bg=entry_bg_color)
my_entry.pack(padx=20, pady=20)
complexity_label = Label(lf, text="Select Complexity:", bg=bg_color, fg=fg_color)
complexity_label.pack(padx=20, pady=10)

complexity_options = ["Easy", "Intermediate", "Hard"]
complexity_combo = ttk.Combobox(lf, values=complexity_options, font=("Helvetica", 12))
complexity_combo.pack(padx=20, pady=10)
complexity_combo.set("Easy")  # Set the default complexity level

pw_entry = Entry(root, text='', font=("Helvetica", 24), bd=0, bg=entry_bg_color)
pw_entry.pack(pady=20)

my_frame = Frame(root, bg=bg_color)
my_frame.pack(pady=20)

my_button = Button(my_frame, text="Generate Strong Password", command=new_rand, bg=button_color)
my_button.grid(row=0, column=0, padx=10)

click_button = Button(my_frame, text="Copy to Clipboard", command=clipper, bg=button_color)
click_button.grid(row=0, column=1, padx=10)

root.mainloop()
