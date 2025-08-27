import tkinter as tk
from tkinter import ttk


class CalcWindow:
    def pressed_0(self):
        self.digits = self.digits * 10 + 0
        self.update_entry()

    def pressed_1(self):
        self.digits = self.digits * 10 + 1
        self.update_entry()

    def pressed_2(self):
        self.digits = self.digits * 10 + 2
        self.update_entry()

    def pressed_3(self):
        self.digits = self.digits * 10 + 3
        self.update_entry()

    def pressed_4(self):
        self.digits = self.digits * 10 + 4
        self.update_entry()

    def pressed_5(self):
        self.digits = self.digits * 10 + 5
        self.update_entry()

    def pressed_6(self):
        self.digits = self.digits * 10 + 6
        self.update_entry()

    def pressed_7(self):
        self.digits = self.digits * 10 + 7
        self.update_entry()

    def pressed_8(self):
        self.digits = self.digits * 10 + 8
        self.update_entry()

    def pressed_9(self):
        self.digits = self.digits * 10 + 9
        self.update_entry()

    def update_entry(self):
        d = str(self.digits)
        self.set_entry(d)

    def set_entry(self, text):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, text)


    def op_mul(self ):
        if self.acc is None:
            self.acc = self.digits
            self.digits = 0

        self.op = '*'

    def op_result(self):
        if self.op == '*':
            res = self.acc * self.digits
        elif self.op == '+':
            res = self.acc + self.digits
        elif self.op == '-':
            res = self.acc - self.digits
        elif self.op == '/':
            if self.digits == 0:
                self.set_entry('ERROR!')
                self.digits = 0
                self.acc = 0
                return

            res = self.acc // self.digits
        else:
            res = self.digits

        self.set_entry(str(res))
        self.acc = res
        self.digits = 0
        self.op = ''


    def __init__(self, root):
        self.acc = None
        self.digits = 0
        self.op = ''

        root.title("Calculator")
        root.geometry("400x250")

        digits_frame = ttk.Frame(root)

        digits_frame.grid(row=1, column=0)

        for i, x, y, fnc in [
            (1, 0, 2, self.pressed_1),
            (2, 1, 2, self.pressed_2),
            (3, 2, 2, self.pressed_3),
            (4, 0, 1, self.pressed_4),
            (5, 1, 1, self.pressed_5),
            (6, 2, 1, self.pressed_6),
            (7, 0, 0, self.pressed_7),
            (8, 1, 0, self.pressed_8),
            (9, 2, 0, self.pressed_9),
        ]:
            def button_clicked():
                print(i)

            button = ttk.Button(digits_frame, text=f'{i}', padding=10, command=fnc)

            button.grid(row=y, column=x)

        button = ttk.Button(digits_frame, text="0", padding=10, command=self.pressed_0)
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

        entry = ttk.Entry(result_frame, )
        entry.grid(row=0, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.entry = entry

        button = ttk.Button(result_frame, text="=", padding=10, command=self.op_result)
        button.grid(row=0, column=3, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.update_entry()


root = tk.Tk()
CalcWindow(root)
root.mainloop()
