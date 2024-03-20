import tkinter as tk
from PIL import Image, ImageTk

def update_frame():
    global current_frame
    current_frame = (current_frame + 1) % num_frames
    canvas.itemconfig(img_object, image=frames[current_frame])
    top.after(50, update_frame)  # Decreased interval for faster animation

top = tk.Tk()
canvas = tk.Canvas(top, bg="white", height=600, width=600)

# Open the GIF file
gif = Image.open("gato.gif")
frames = []
num_frames = 0

try:
    while True:
        frames.append(ImageTk.PhotoImage(gif.copy()))
        gif.seek(gif.tell() + 1)
        num_frames += 1
except EOFError:
    pass

# Display the first frame
current_frame = 0
img_object = canvas.create_image(600/2, 600/2, image=frames[current_frame])

# Start the animation
update_frame()

canvas.pack(expand=1)
top.mainloop()
