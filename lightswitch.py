import tkinter as tk
window = tk.Tk()

# button = tk.Button(text='...', bg="white", fg="black")
# button.pack(pady = 20, padx = 20)

# schijf hier tussen je code

KnopUit_Aan = True

def KnopTekst():
    if button.config("text")[-1] == "switch light on":
        button.config(text="switch light off")
        print ("light is on")
    else:
        button.config(text="switch light on")
        print ("light is off")

def KleurKnop():
    if window.config("background")[-1] == "yellow":
        window.config(background='black')
    else:
        window.config(background='yellow')
        



# if KnopUit_Aan == True:
button = tk.Button(text='switch Light off', command=KnopTekst)
button.pack(pady = 20, padx = 20)
window.config(background=KleurKnop())
KnopUit_Aan = False


# elif KnopUit_Aan == False:
#     button = tk.Button(text='Switch Light off', command=PrintUit_Aan)
#     button.pack(pady = 20, padx = 20)
#     window.configure(background='yellow')
#     KnopUit_Aan = True


# schijf hier tussen je code

window.mainloop()
