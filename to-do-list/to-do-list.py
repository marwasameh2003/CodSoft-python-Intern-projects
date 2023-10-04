import tkinter
from tkinter import *

root = Tk()
root.title("To-Do-List")
root.geometry("400x600+400+100")
root.resizable(False, False)

task_list = []

def addtask():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open("Tasklist.txt", "a") as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END,task)

def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("Tasklist.txt","w") as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")
        listbox.delete(ANCHOR)
def opentaskfile():
    try:
        global task_list
        with open("Tasklist.txt","r") as taskfile:
            tasks = taskfile.readlines()
        
        for task in tasks:
            if task != '\n':
                task_list.append(task)
                listbox.insert(END,task)
    except:
        file = open('Tasklist.txt','w')
        file.close()

def markFinished():
    selected_task = listbox.get(ANCHOR)
    if selected_task:
        index = task_list.index(selected_task)
        task_list[index] = "[Finished] " + selected_task
        updateTaskList()
        
def editTask():
    selected_task = listbox.get(ANCHOR)
    if selected_task:
        task_entry.delete(0, END)
        task_entry.insert(0, selected_task)
        deleteTask()
        task_entry.focus()

def updateTaskList():
    listbox.delete(0, END)
    for task in task_list:
        listbox.insert(END, task)
image_icon = PhotoImage(file ="images/task.png")
root.iconphoto(False,image_icon )

topimage = PhotoImage(file="images/topbar.png")
Label(root, image=topimage).pack()

dockimage = PhotoImage(file="images/dock.png")
Label(root, image=dockimage, bg="#32405b").place(x=30,y=25)

noteimage = PhotoImage(file="images/task.png")
Label(root, image=noteimage, bg="#32405b").place(x=340, y=25)

heading= Label(root, text="All TASKS", font="arial 20 bold", fg="white",bg="#32405b")
heading.place(x=130, y=20)

frame =Frame(root, width=400, height=50, bg="white")
frame.place(x=0, y=180)

task = StringVar()
task_entry = Entry(frame,width=18, font="arial 20",bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()


button = Button(frame, text="ADD",font="arial 20 bold",width=6, bg="#5a95ff",fg="#fff", bd=0,command=addtask)
button.place(x=300, y=0)

frame1 = Frame(root, bd=3, width=700, height=280, bg="#32405b")
frame1.pack(pady=(160, 0))

listbox = Listbox(frame1, font=('arial', 12), width=40, height=14, bg="#32405b", fg="white", cursor="hand2",
                  selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Buttons for Mark as Finished and Edit Task
finish_button = Button(root, text="Mark as Finished", font="arial 12 bold", width=16, bg="#5a95ff", fg="#fff",
                       bd=0, command=markFinished)
finish_button.pack(side=LEFT, padx=(20, 0))

edit_button = Button(root, text="Edit Task", font="arial 12 bold", width=10, bg="#5a95ff", fg="#fff",
                     bd=0, command=editTask)
edit_button.pack(side=LEFT)


opentaskfile()
delete_icon = PhotoImage(file="images/delete.png")
Button(root, image=delete_icon, bd=0, command=deleteTask).pack(side=BOTTOM,pady=13)
root.mainloop()