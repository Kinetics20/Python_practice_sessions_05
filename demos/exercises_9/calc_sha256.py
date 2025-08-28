import tkinter as tk
from tkinter import ttk
import hashlib
import binascii


class SHA256Calculator:
    def __init__(self, root):
        root.title("SHA256 Calculator")
        root.geometry("600x200")

        input_frame = ttk.Frame(root)
        input_frame.pack(fill="x", pady=5, padx=5)

        ttk.Label(input_frame, text="Enter input here:").pack(side="left", padx=5)

        self.entry = ttk.Entry(input_frame, width=50)
        self.entry.pack(side="left", fill="x", expand=True, padx=5)

        self.mode = tk.StringVar(value="text")

        mode_frame = ttk.Frame(root)
        mode_frame.pack(fill="x", pady=5)

        ttk.Radiobutton(mode_frame, text="Text", variable=self.mode, value="text").pack(side="left", padx=5)
        ttk.Radiobutton(mode_frame, text="Hex", variable=self.mode, value="hex").pack(side="left", padx=5)

        button = ttk.Button(root, text="Calculate SHA256 hash", command=self.calculate)
        button.pack(fill="x", pady=10, padx=5)

        result_frame = ttk.Frame(root)
        result_frame.pack(fill="x", pady=5, padx=5)

        ttk.Label(result_frame, text="SHA256 Hash:").pack(side="left", padx=5)

        self.result = ttk.Entry(result_frame, width=70)
        self.result.pack(side="left", fill="x", expand=True, padx=5)

    def calculate(self):
        text = self.entry.get()
        try:
            if self.mode.get() == "text":
                data = text.encode("utf-8")
            else:
                data = binascii.unhexlify(text.strip())

            sha256_hash = hashlib.sha256(data).hexdigest()
            self.result.delete(0, tk.END)
            self.result.insert(0, sha256_hash)
        except Exception as e:
            self.result.delete(0, tk.END)
            self.result.insert(0, f"Error: {e}")


root = tk.Tk()
SHA256Calculator(root)
root.mainloop()
