from tkinter import *

window = Tk()

def convert():
    text_grams.insert(END, float(entry_text.get()) * 1000)
    text_pounds.insert(END, float(entry_text.get()) * 2.20462)
    text_ounces.insert(END, float(entry_text.get()) * 35.274)

label = Label(window, text="Kg")
label.grid(row=0, column=0)

entry_text = StringVar()
entry = Entry(window, textvariable=entry_text)
entry.grid(row=0, column=1)

button = Button(window, text="Convert", command=convert)
button.grid(row=0, column=2)

text_grams = Text(window, height=1, width=20)
text_grams.grid(row=1, column=0)

text_pounds = Text(window, height=1, width=20)
text_pounds.grid(row=1, column=1)

text_ounces = Text(window, height=1, width=20)
text_ounces.grid(row=1, column=2)

window.mainloop()
