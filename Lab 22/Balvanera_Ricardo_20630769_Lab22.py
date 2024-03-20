import tkinter as tk
import tkinter.font as font

w = tk.Tk()

w.geometry("500x200")

fontStyle = font.Font(family="Batman", size=20)
hello = tk.Label(text="Hello Ricardo",
                 foreground="black",
                 background="blue",
                 width=20,
                 height=2,
                 font=fontStyle)

hello.pack()

w.mainloop()
