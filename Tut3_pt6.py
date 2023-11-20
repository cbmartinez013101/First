# entry widget =textbox that accepts a single line of user input

from tkinter import *

def submit():
    username=entry.get()
    print('Hello'+username)

def delete():
    entry.delete(0,END) #Deletes line of text

def backspace():
    entry.delete(len(entry.get())-1,END) #delete last character

window = Tk()
window.title('user input')
label=Label(window,text='username:')
label.config(font=('Consolas',30))
label.pack(side=LEFT)

submit=Button(window,text='submit',command=submit)
submit.pack(side=RIGHT)

backspace=Button(window,text='backspace',command=backspace)
backspace.pack(side=RIGHT)

delete=Button(window,text='delete',command=delete)
delete.pack(side=RIGHT)

entry=Entry()
entry.config(font=('Ink Free',50))
entry.config(bg='#111111')
entry.config(fg='#00ff00')
#entry.insert(0,'Spongebob')
#entry.config(state=DISABLED) #active or disabled
entry.config(width=10)

entry.pack()
window.mainloop()
