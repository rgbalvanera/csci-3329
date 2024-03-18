import tkinter as tk
import tkinter.font as font

w = tk.Tk()
w.geometry("500x100+300+600")

fontStyle = font.Font(family="Batman", size=20)
hello = tk.Label(w, text="Hello Ricardo", font=fontStyle)
hello.pack()

w.mainloop()
