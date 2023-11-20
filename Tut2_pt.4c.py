from tkinter import*

def changebackgroundColor(event):
    firstColors["bg"]=firstColors.get(firstColors.curselection())

window=Tk()
window.title('Colors')

#Below L is just a name for your list of colors
#Whenever you want to refer or list your list of colors
#you refer to the list as L that is the name we gave the list

L=['red', 'yellow', 'light green', 'orange']

conOFlstColors=StringVar()

firstColors=Listbox(window, width=10, heigh=5, listvariable=conOFlstColors)

firstColors.grid(padx=100, pady=15)

conOFlstColors.set(tuple(L))

firstColors.bind("<<ListboxSelect>>", changebackgroundColor)

window.mainloop()
