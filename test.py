# from tkinter import *

# def Simpletoggle():
    
#     if toggle_button.config('text')[-1] == 'ON':
#         toggle_button.config(text='OFF')
#     else:
#         toggle_button.config(text='ON')

# ws = Tk()
# ws.title("Python Guides")
# ws.geometry("200x100")

# toggle_button = Button(text="OFF", width=10, command=Simpletoggle)
# toggle_button.pack(pady=10)

# ws.mainloop()

# ------

# def KleurKnop():
#     if window.config('background')[-1] == 'yellow':
#         window.config(background="black")
#     else:
#         window.config(background="yellow")

# --------

# from tkinter import *   

# tkWindow = Tk()  
# tkWindow.geometry('400x150')  
# tkWindow.title('PythonExamples.org - Tkinter Example')
  
# button = Button(tkWindow, text = 'Submit', bg='yellow', activebackground='red')  
# button.pack()  
  
# tkWindow.mainloop()


# --------

import tkinter as tk

class Test():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("250x100")
        self.buttonA = tk.Button(self.root,
                                 text = "Color",
                                 bg = "blue",
                                 fg = "red")

        self.buttonB = tk.Button(self.root,
                                text="Click to change color",
                                bg = "gray",
                                fg = "purple")
        self.buttonA.pack(side=tk.LEFT)
        self.buttonB.pack(side=tk.RIGHT)
        self.root.mainloop()     

app=Test()