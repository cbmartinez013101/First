#A List box that displays a list of colors

from tkinter import*

window=Tk()
window.title('Colors')

L=['orange', 'red', 'yellow', 'light blue']
conOFlstColors=StringVar() #contents of the list box

firstColors=Listbox(window, width=10, height=5, listvariable=conOFlstColors)

firstColors.grid(padx=100, pady=20)

conOFlstColors.set(tuple(L))# a tupleis a none editing list of items
window.mainloop()
