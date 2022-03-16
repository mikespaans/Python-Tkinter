import tkinter as tk
window = tk.Tk()

button = tk.Button(text='...', bg="white", fg="black")
button.pack(pady = 20, padx = 20)

# schijf hier tussen je code

KnopUit_Aan = True

def KnopTekst():
    if button.config("text")[-1] == "switch light on":
        button.config(text="switch light off")
        window.config(background='yellow')

        print ("light is on")
    else:
        button.config(text="switch light on")
        window.config(background='black')

        print ("light is off")


        



button = tk.Button(text='switch Light off', command=KnopTekst)
button.pack(pady = 20, padx = 20)
window.config(background=KnopTekst())



# schijf hier tussen je code

window.mainloop()