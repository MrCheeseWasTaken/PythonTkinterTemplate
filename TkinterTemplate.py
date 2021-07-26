from tkinter import *

cellsize = 50
height = cellsize*10
width = cellsize*10

BgColor = "#000000"

window = Tk()
window.title("Template")
window.resizable(False, False)

canvas = Canvas(window, bg=BgColor, height=height, width=width, highlightthickness=0)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.mainloop()