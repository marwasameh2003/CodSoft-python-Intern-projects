import tkinter as tk

def addNumtoScreen(num):
    t = empty_box.cget("text")  # Get the current text of the box
    t += num  # Append the clicked number to the text
    empty_box.config(text=t)

def performOperation():
    t = empty_box.cget("text")
    try:
        result = str(eval(t))
        empty_box.config(text=result)
    except:
        empty_box.config(text="Error")

def clearBox():
    empty_box.config(text="")

def main():
    global root
    root = tk.Tk()
    # Set window size
    window_width = 400
    window_height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
    root.title("Calculator")
    background_color = "#FFBFBF"  # Light gray
    root.configure(bg=background_color)
    text = "Calculator"
    text_label = tk.Label(root, text=text, fg="#1A5D1A", bg="#FFBFBF", font=("Helvetica", 16, "bold"))
    text_label.pack(pady=20)
    box_frame = tk.Frame(root, bg=background_color)
    box_frame.pack()

    global empty_box
    empty_box = tk.Label(box_frame, bg="#F3FDE8", width=24, height=2, font=("Helvetica", 16))
    empty_box.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    txt_list = [
        "7", "8", "9", "/",
        "4", "5", "6", "*",
        "1", "2", "3", "-",
        "C", "0", "=", "+"
    ]

    row = 1
    col = 0
    for txt in txt_list:
        if txt == "=":
            cmd = performOperation
        elif txt == "C":
            cmd = clearBox
        else:
            cmd = lambda t=txt: addNumtoScreen(t)

        button = tk.Button(box_frame, text=txt, command=cmd, bg="#F3FDE8", fg="#1A5D1A", font=("Helvetica", 16))
        button.config(width=6, height=2, borderwidth=0, relief="flat", highlightthickness=0, padx=0)
        button.grid(row=row, column=col, padx=5, pady=5)
        col += 1
        if col > 3:
            col = 0
            row += 1

    root.mainloop()

main()
