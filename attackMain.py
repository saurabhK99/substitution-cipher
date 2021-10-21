from tkinter import *
from attack import *

#calls letter frequency attack 
def attack(on, cipherTxt):
    plainTxt = str()
    attack = LetterFrequencyAttack(cipherTxt, on)
     
    for i in range(10):
        plainTxt = plainTxt + attack.attack() + '\n\n'
        answer.config(text = plainTxt)
    
#defining main window
root = Tk()
root.title('Letter Frequency Attack')
root.configure(
    background='#221b1b',
)
root.option_add('*Font', 'helvatica 12')
root.option_add('*Foreground', 'whitesmoke')
root.option_add('*Background', '#221b1b')
root.option_add('*Entry.HighlightColor', 'whitesmoke')

#key value pairs for radio buttons
types = [
    ('MONOALPHABETIC_CIPHER', 'MONOALPHABETIC_CIPHER'),
    ('ADDITIVE_CIPHER', 'ADDITIVE_CIPHER') 
]

#variable to store current selection of radio button
attackOn= StringVar()
attackOn.set('MONOALPHABETIC_CIPHER')

Label(root, text='ATTACK ON').grid(row=0, column=0, padx=20)

#radio buttons
for i in range(2):
    Radiobutton(
        root, 
        text=types[i][0],
        value=types[i][1], 
        variable=attackOn,
        highlightthickness=0,
        activebackground='#221b1b',
        activeforeground='whitesmoke'
    ).grid(
        row=0, 
        column=i+1, 
        padx=20,
        pady=20
    )

#label to show the result
answer = Label(root, text='ANSWER HERE', wraplength=700, justify=CENTER)
answer.grid(row=1, column=0, columnspan=3, pady=20)

#entry widget to input cipher text to crack
Label(root, text='CIPHER TXT').grid(row=6, column=0)
cipherTxt = Entry(root)
cipherTxt.grid(row=6, column=1, columnspan=2, pady=20)

#button to call attack()
Button(
    root,
    text='DECRYPT', 
    justify=CENTER,
    command=lambda: attack(
        attackOn.get(),
        cipherTxt.get()
    )
).grid(
    row=7, 
    column=0,
    columnspan=3, 
    pady=20
)

#mainloop of tkinter window
root.mainloop()
