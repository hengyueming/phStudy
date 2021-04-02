import tkinter as tk 
from tkinter import filedialog, Text
import os

root = tk.Tk()

canvas = tk.Canvas(root, height=800, width= 600, bg = 'Blue')
canvas.pack()


frame = tk.Frame(root, bg='White')
frame.place(relwidth=0.8, relheight=0.8, relx = 0.1, rely = 0.1)

openFile = tk.Button(root, text = 'Open Image', padx = 10, pady = 5, fg= 'white', bg = 'grey')
openFile.pack()



root.mainloop()
