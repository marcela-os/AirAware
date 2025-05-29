import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def launch_gui():
    # app = ttk.Window(themename="flatly")
    # app.title("Air Monitor")
    # app.geometry("400x200")
    #
    # refresh = RefreshFrame(app)
    # refresh.pack(padx=10, pady=20, fill=tk.BOTH, expand=True)
    #
    # app.mainloop()


    root = tk.Tk()
    root.title("Tk Example")
    root.configure(background="yellow")
    root.minsize(200, 200)
    root.maxsize(500, 500)
    root.geometry("300x300+50+50")
    b1 = ttk.Button(root, text="Button 1", bootstyle=SUCCESS)
    b1.pack(side=LEFT, padx=5, pady=10)

    b2 = ttk.Button(root, text="Button 2", bootstyle=(INFO, OUTLINE))
    b2.pack(side=LEFT, padx=5, pady=10)

    v = tk.StringVar()
    label1 = tk.Label(root,
                      textvariable=v,
                      padx=10,
                      pady=10)
    label1.pack()
    entry1 = tk.Entry(root, width=50, textvariable=v)
    entry1.pack(padx=10, pady=10)

    def f1():
        v.set('')

    b1 = tk.Button(root, text="Clear", command=f1)
    b1.pack(padx=10, pady=10)

    root.mainloop()
