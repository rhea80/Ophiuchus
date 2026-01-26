import tkinter as tk
import time

class pet():
    def __init__(self):
        self.window = tk.Tk()
        img = tk.PhotoImage(file='image.png')
        self.window.config(highlightbackground='black')
        self.window.overrideredirect(True)
        self.window.attributes('-topmost', True)
        self.window.wm_attributes('-transparentcolor', 'black')
        self.label = tk.Label(self.window, bd=0, bg='black')
        self.window.geometry('128x128+0+0')
        self.label.configure(image=img)
        self.label.pack()
        self.window.after(0, self.update)
        self.window.mainloop()

    def update(self):
        self.window.after(10, self.update)

pet()