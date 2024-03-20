import tkinter as tk
from PIL import Image, ImageTk
top = tk.Tk()
c = tk.Canvas(top, bg='black', height=800,
width=800)
load = Image.open('fatchocobo.png')
img = ImageTk.PhotoImage(load)
c.create_image(800/2, 800/2, image=img)
c.pack()
top.mainloop()