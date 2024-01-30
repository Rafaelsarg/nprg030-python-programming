from tkinter import *
from tkcalendar import *
from tkinter import messagebox
import json
import os


data = {}

if not os.path.isfile('memory.json'):
    with open('memory.json','w') as f:
        json.dump(data,f)

with open('memory.json','r') as f:
    all_tasks = json.load(f)


root = Tk()
root.geometry('1000x500')
root.title('ToDo')
root.config(bg='#3C474B')

bottomframe = Frame(root, bg='#3C474B')
rightframe = Frame(root, bg='#3C474B')
leftframe = Frame(root, bg='#3C474B')

def refreshPage():
    date = cal.get_date()
    if date in all_tasks:    
        for i in all_tasks[date]:
            lb.insert(END, i)

def openWrite():
    with open('memory.json', 'w') as f:
            json.dump(all_tasks, f)


def addTask():
    if entry.get() == '':
        messagebox.showwarning('Warning', 'Please Insert Something')
        return
    lb.insert(END, entry.get())
    ent = entry.get()
    entry.delete(0,END)
    date = cal.get_date()
    if date in all_tasks:
        all_tasks[date].append(ent)
    else:
        all_tasks[date] = [ent] 
    openWrite()
   

    
def deleteTask():
    if lb.get(ANCHOR) == '':
        messagebox.showwarning('Warning','Please select item to delete.')
        return
    word = lb.get(ANCHOR)
    lb.delete(ANCHOR)
    date = cal.get_date()
    all_tasks[date].remove(word)
    openWrite()


def editTask():
    if entry.get() != '':
        messagebox.showwarning('Warning', 'You have text in Entry')
    else:
        word = lb.get(ANCHOR)
        entry.insert(0,word)

def onClick(event):
    date = cal.get_date()
    if date in all_tasks:
        lb.delete(0,END)
        for i in all_tasks[date]:
            lb.insert(END,i)
    else:
        lb.delete(0,END)


def replaceEdited():
    if(lb.get(ANCHOR) == ''):
        messagebox.showwarning('Warning','Please Select an item to replace')
    elif(entry.get() == ''):
        messagebox.showwarning('Warning', 'No text in Entry')    
    else:    
        word = entry.get()
        date = cal.get_date()
        selected = lb.get(ANCHOR)
        for i in range(len(all_tasks[date])):
            if(all_tasks[date][i] == selected):
                all_tasks[date][i] = word
                break
        openWrite()
        entry.delete(0,END)
        lb.delete(0,END)
        refreshPage()


cal = Calendar(leftframe, font='Arial 15', selectmode='day', cursor='hand2')
cal.pack(padx=40)

sc = Scrollbar(rightframe, orient='vertical')
sc.pack(side= RIGHT, fill=BOTH)

lb = Listbox(
    rightframe,
    width=30,
    height=10,
    font=('Times New Roman', 18),
    bd=5,
    highlightthickness=0,
    activestyle='none',
    yscrollcommand=sc.set
    
)
lb.pack(pady=30, padx=40)

sc.config(command=lb.yview)

entry = Entry(rightframe, width = 40, font = ('Times New Roman',18))
entry.pack(pady=10, padx=20)

refreshPage()

def button(text, command):
    b = Button(rightframe, text=text, command=command)
    b.pack(side=LEFT,padx=5)
    return b

addBtn = button('Add Task', addTask)
deleteBtn = button('Delete Task', deleteTask)
editBtn = button('Edit Task', editTask)
addEdit = button('Add Edited', replaceEdited)

leftframe.pack(side=LEFT)
rightframe.pack(side=RIGHT, fill=BOTH)

root.bind('<<CalendarSelected>>',onClick)
root.resizable(False, False)
root.mainloop()