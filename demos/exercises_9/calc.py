import tkinter as tk
from tkinter import ttk


class CalcWindow:
    def __init__(self, root):
        root.title("Calculator")
        root.geometry("800x600")

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        frame = ttk.Frame(root)
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        buttons = []
        for i in range(0, 10):
            button = ttk.Button(frame, text=f'{i}')
            buttons.append(button)

        for i, x, y in [
            (1, 0, 2),
            (2, 1, 2),
            (3, 2, 2),
            (4, 0, 1),
            (5, 1, 1),
            (6, 2, 1),
            (7, 0, 0),
            (8, 1, 0),
            (9, 2, 0),
        ]:
            buttons[i].grid(row=y, column=x)

        button = ttk.Button(frame, text="0")
        button.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S))





root = tk.Tk()
CalcWindow(root)
root.mainloop()