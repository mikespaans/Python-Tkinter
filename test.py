# import tkinter as tk
# from tkinter import ttk


# def return_pressed(event):
#     print('Return key pressed.')


# root = tk.Tk()

# btn = ttk.Button(root, text='Save')
# btn.bind('<Return>', return_pressed)


# btn.focus()
# btn.pack(expand=True)

# root.mainloop()

from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("My App")
root.config(bg="#ff0000")

def printhi(*args):
	print("Hi!")
    
btn = Button(root, text="Click to print hi", command=printhi)
btn.place(x=200, y=200)

root.mainloop()