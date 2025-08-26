import tkinter as tk
from tkinter import ttk


class CalcWindow:
    def __init__(self, root):
        root.title("Calculator")
        root.geometry("800x600")

        # root.columnconfigure(0, weight=1)
        # root.rowconfigure(0, weight=1)

        # result_frame = ttk.Frame(root)
        # result_frame.grid(row=0, column=0, columnspan=2)
        #
        # entry = ttk.Entry(root)
        # entry.grid(row=0, column=0, sticky = (tk.W, tk.E, tk.N, tk.S))

        digits_frame = ttk.Frame(root)
        digits_frame.grid(row=1, column=0)

        # sticky = (tk.W, tk.E, tk.N, tk.S)

        buttons = []
        for i in range(0, 10):
            button = ttk.Button(digits_frame, text=f'{i}', padding=10)
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

        button = ttk.Button(digits_frame, text="0", padding=10)
        button.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S))


        ops_frame = ttk.Frame(root)
        ops_frame.grid(row=1, column=1)

        for i, op in enumerate([
            '+', '-', '*', '/'
        ]):

            button = ttk.Button(ops_frame, text=op, padding=10)
            button.grid(row=i, column=0)

        result_frame = ttk.Frame(root)
        result_frame.grid(row=0, column=0, columnspan=2)

        entry = ttk.Entry(root, state='readonly')
        entry.grid(row=0, column=0, sticky = (tk.W, tk.E, tk.N, tk.S))


root = tk.Tk()
CalcWindow(root)
root.mainloop()