import tkinter as tk
window = tk.Tk()

button = tk.Button(text='...', bg="white", fg="black")
button.pack(pady = 20, padx = 20)

# schijf hier tussen je code

KnopUit_Aan = False

def PrintUit_Aan():
        if KnopUit_Aan == True:
            print ("light is off")
        elif KnopUit_Aan == False:
            print ("light is on")


# while Doorgaan == True:
if KnopUit_Aan == True:
    button = tk.Button(text='Switch Light on', command=PrintUit_Aan)
    button.pack(pady = 20, padx = 20)
    window.configure(background='black')
    KnopUit_Aan = False


elif KnopUit_Aan == False:
    button = tk.Button(text='Switch Light off', command=PrintUit_Aan)
    button.pack(pady = 20, padx = 20)
    window.configure(background='yellow')
    KnopUit_Aan = True
# schijf hier tussen je code

window.mainloop()
