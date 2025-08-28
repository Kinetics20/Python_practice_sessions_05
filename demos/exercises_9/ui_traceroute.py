import tkinter as tk
from tkinter import ttk
import subprocess
import threading


class TracerouteUI:
    def __init__(self, root):
        root.title("Traceroute UI")
        root.geometry("800x600")

        # --- Host input ---
        host_frame = ttk.Frame(root)
        host_frame.pack(fill="x", pady=5, padx=5)

        ttk.Label(host_frame, text="Host:").pack(side="left", padx=5)
        self.host_entry = ttk.Entry(host_frame, width=50)
        self.host_entry.pack(side="left", fill="x", expand=True, padx=5)

        # --- Options ---
        options_frame = ttk.LabelFrame(root, text="Options")
        options_frame.pack(fill="x", pady=5, padx=5)

        self.no_dns = tk.BooleanVar(value=False)
        ttk.Checkbutton(
            options_frame,
            text="No reverse DNS name resolution",
            variable=self.no_dns
        ).pack(side="left", padx=5)

        ttk.Label(options_frame, text="Maximum number of hops:").pack(side="left", padx=5)
        self.max_hops = ttk.Entry(options_frame, width=5)
        self.max_hops.insert(0, "30")
        self.max_hops.pack(side="left", padx=5)

        # --- Button ---
        self.start_button = ttk.Button(
            root,
            text="Start tracing the route",
            command=self.start_traceroute
        )
        self.start_button.pack(fill="x", pady=10, padx=5)

        # --- Output ---
        output_frame = ttk.LabelFrame(root, text="Output")
        output_frame.pack(fill="both", expand=True, padx=5, pady=5)

        self.output = tk.Text(
            output_frame,
            wrap="word",
            bg="black",
            fg="lime",
            insertbackground="white"
        )
        self.output.pack(fill="both", expand=True)

    def start_traceroute(self):
        host = self.host_entry.get().strip()
        hops = self.max_hops.get().strip()

        if not host:
            self.append_output("Please enter a host!\n")
            return

        cmd = ["tracepath", host]

        if hops.isdigit():
            cmd.extend(["-m", hops])
        if self.no_dns.get():
            cmd.append("-n")

        self.append_output(f"Running: {' '.join(cmd)}\n\n")

        # Run traceroute in separate thread
        thread = threading.Thread(target=self.run_command, args=(cmd,))
        thread.daemon = True
        thread.start()

    def run_command(self, cmd):
        try:
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True
            )
            for line in process.stdout:
                self.append_output(line)
        except Exception as e:
            self.append_output(f"Error: {e}\n")

    def append_output(self, text):
        self.output.insert(tk.END, text)
        self.output.see(tk.END)


root = tk.Tk()
TracerouteUI(root)
root.mainloop()
