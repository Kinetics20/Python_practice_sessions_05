import tkinter as tk
from tkinter import ttk
import math


class CalcWindow:
    def __init__(self, root):
        self.acc = None
        self.digits = ""
        self.op = ""

        root.title("Calculator")
        root.geometry("400x300")

        digits_frame = ttk.Frame(root)
        digits_frame.grid(row=1, column=0)

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
            button = ttk.Button(
                digits_frame,
                text=f'{i}',
                padding=10,
                command=lambda d=i: self.press_digit(d)
            )
            button.grid(row=y, column=x)

        button = ttk.Button(digits_frame, text="0", padding=10, command=lambda: self.press_digit(0))
        button.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))

        button = ttk.Button(digits_frame, text=".", padding=10, command=self.press_dot)
        button.grid(row=3, column=2, sticky=(tk.W, tk.E, tk.N, tk.S))

        ops_frame = ttk.Frame(root)
        ops_frame.grid(row=1, column=1)

        for i, (op, fcn) in enumerate([
            ('+', lambda: self.set_op('+')),
            ('-', lambda: self.set_op('-')),
            ('*', lambda: self.set_op('*')),
            ('/', lambda: self.set_op('/')),
            ('√', self.op_sqrt),
            ('^', lambda: self.set_op('^'))
        ]):
            button = ttk.Button(ops_frame, text=op, padding=10, command=fcn)
            button.grid(row=i, column=0)

        result_frame = ttk.Frame(root)
        result_frame.grid(row=0, column=0, columnspan=2)

        self.entry = ttk.Entry(result_frame)
        self.entry.grid(row=0, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S))

        button = ttk.Button(result_frame, text="=", padding=10, command=self.op_result)
        button.grid(row=0, column=3, sticky=(tk.W, tk.E, tk.N, tk.S))

        button = ttk.Button(result_frame, text="C", padding=10, command=self.clear)
        button.grid(row=0, column=4, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.update_entry()

    def press_digit(self, d):
        self.digits += str(d)
        self.update_entry()

    def press_dot(self):
        if '.' not in self.digits:
            if self.digits == "":
                self.digits = "0."
            else:
                self.digits += "."
        self.update_entry()

    def update_entry(self):
        self.set_entry(self.digits if self.digits else "0")

    def set_entry(self, text):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, text)

    def clear(self):
        self.acc = None
        self.digits = ""
        self.op = ""
        self.update_entry()

    def set_op(self, op):
        if self.digits != "":
            if self.acc is None:
                self.acc = float(self.digits)
            else:
                self.op_result()
        self.op = op
        self.digits = ""
        self.update_entry()

    def op_sqrt(self):
        if self.digits != "":
            val = float(self.digits)
        elif self.acc is not None:
            val = self.acc
        else:
            return
        if val < 0:
            self.set_entry("ERROR")
            self.digits = ""
            self.acc = None
            return
        res = math.sqrt(val)
        self.set_entry(str(res))
        self.acc = res
        self.digits = ""

    def op_result(self):
        if self.op and self.digits != "":
            b = float(self.digits)
            if self.op == '+':
                res = self.acc + b
            elif self.op == '-':
                res = self.acc - b
            elif self.op == '*':
                res = self.acc * b
            elif self.op == '/':
                if b == 0:
                    self.set_entry("ERROR")
                    self.clear()
                    return
                res = self.acc / b
            elif self.op == '^':
                res = self.acc ** b
            else:
                res = b
            self.set_entry(str(res))
            self.acc = res
            self.digits = ""
            self.op = ""


root = tk.Tk()
CalcWindow(root)
root.mainloop()
