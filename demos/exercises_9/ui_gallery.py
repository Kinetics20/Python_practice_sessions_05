import tkinter as tk
from tkinter import ttk


class UIGallery:
    def __init__(self, root):
        root.title("UI Gallery")
        root.geometry("400x300")

        self.label = ttk.Label(root, text="This is a text label.")
        self.label.pack(pady=5)

        self.button = ttk.Button(root, text="Click me", command=self.on_button_click)
        self.button.pack(pady=5)

        self.entry = ttk.Entry(root)
        self.entry.pack(pady=5)

        self.check_var = tk.BooleanVar()
        self.checkbox = ttk.Checkbutton(root, text="Check me", variable=self.check_var, command=self.on_check)
        self.checkbox.pack(pady=5)

        self.combo = ttk.Combobox(root, values=["Cat", "Dog", "Fish", "Lizard"])
        self.combo.pack(pady=5)

        self.listbox = tk.Listbox(root, height=4)
        for item in ["Red", "Green", "Blue", "Yellow"]:
            self.listbox.insert(tk.END, item)
        self.listbox.pack(pady=5)
        self.listbox.bind("<<ListboxSelect>>", self.on_list_select)

    def on_button_click(self):
        text = self.entry.get()
        if not text:
            text = "Entry is empty!"
        self.label.config(text=f"Button clicked: {text}")

    def on_check(self):
        state = "checked" if self.check_var.get() else "unchecked"
        self.label.config(text=f"Checkbox is {state}")

    def on_list_select(self, event):
        if not self.listbox.curselection():
            return
        value = self.listbox.get(self.listbox.curselection())
        self.label.config(text=f"Listbox selected: {value}")


root = tk.Tk()
UIGallery(root)
root.mainloop()
