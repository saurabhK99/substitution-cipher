from tkinter import * 
from cipher import *

#calls different encryption algorithms
def encrypt(algo, plainTxt, *keys):
    if algo == 1:
        add = AdditiveCipher(keys[0])
        answer.config(text = add.encrypt(plainTxt))

    elif algo == 2:
        aff = AffineCipher(keys[0], keys[1])
        answer.config(text = aff.encrypt(plainTxt))

    elif algo == 3:
        hill = HillCipher(keys)
        answer.config(text = hill.encrypt(plainTxt))


#calls different decryption algorithms
def decrypt(algo, cipherTxt, *keys):
    if algo == 1:
        add = AdditiveCipher(keys[0])
        answer.config(text = add.decrypt(cipherTxt))

    elif algo == 2:
        aff = AffineCipher(keys[0], keys[1])
        answer.config(text = aff.decrypt(cipherTxt))

    elif algo == 3:
        hill = HillCipher(keys)
        answer.config(text = hill.decrypt(cipherTxt))


#defining main window 
root = Tk()
root.title('ENCRYPTION ALGORITHM')
root.configure(
    background='#221b1b',
)
root.option_add('*Font', 'helvatica 12')
root.option_add('*Foreground', 'whitesmoke')
root.option_add('*Background', '#221b1b')
root.option_add('*Entry.HighlightColor', 'whitesmoke')


#key value pairs for radio buttons
algorithms = [
    ('ADDITIVE CIPHER', 1),
    ('AFFINE CIPHER', 2),
    ('HILL CIPHER', 3), 
]

#variable to store current selection of radio button
currentAlgorithm = IntVar()
currentAlgorithm.set(1)

#radio buttons
for i in range(3):
    Radiobutton(
        root, 
        text=algorithms[i][0],
        value=algorithms[i][1], 
        variable=currentAlgorithm,
        highlightthickness=0,
        activebackground='#221b1b',
        activeforeground='whitesmoke'
    ).grid(
        row=0, 
        column=i, 
        padx=20,
        pady=10
    )


#label to show the result
answer = Label(root, text='ANSWER HERE', wraplength=700, justify=CENTER)
answer.grid(row=1, column=0, columnspan=3, pady=20)

#entry widgets to input keys
Label(root, text='KEY1').grid(row=2, column=0)
key1 = Entry(root, justify=CENTER, bd=0)
key1.grid(row=2, column=1, columnspan=2, pady=10)

Label(root, text='KEY2').grid(row=3, column=0)
key2 = Entry(root, justify=CENTER, bd=0)
key2.grid(row=3, column=1, columnspan=2, pady=10)

Label(root, text='KEY3').grid(row=4, column=0)
key3 = Entry(root, justify=CENTER, bd=0)
key3.grid(row=4, column=1, columnspan=2, pady=10)

Label(root, text='KEY4').grid(row=5, column=0)
key4 = Entry(root, justify=CENTER, bd=0)
key4.grid(row=5, column=1, columnspan=2, pady=10)

#entry widget to input the text to encrypt/decrypt
Label(root, text='INPUT TXT').grid(row=6, column=0)
inputTxt = Entry(root, bd=0)

inputTxt.grid(
    row=6,
    column=1, 
    columnspan=2,
    pady=20
)

#button to call encrypt()
Button(
    root,
    text='Encrypt',
    relief='flat', 
    command=lambda: encrypt(
        currentAlgorithm.get(),
        inputTxt.get(),
        int(key1.get() or 0),
        int(key2.get() or 0),
        int(key3.get() or 0),
        int(key4.get() or 0)
    )
).grid(row=7, column=0, pady=10)


#button to call decrypt()
Button(
    root,
    text='Decrypt', 
    relief='flat',
    command=lambda: decrypt(
        currentAlgorithm.get(),
        inputTxt.get(),
        int(key1.get() or 0),
        int(key2.get() or 0),
        int(key3.get() or 0),
        int(key4.get() or 0)
    )
).grid(row=7, column=2, pady=10)

#mainloop of tkinter window
root.mainloop()