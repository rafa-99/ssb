import os
import tkinter as tk
import tkinter.filedialog


class ExecutableFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.path = tk.StringVar(value="")
        self.display = tk.StringVar(value="None")

        tk.Button(
            self,
            text="Select Executable",
            command=self.select_file
        ).pack(side="left", padx=5)

        tk.Label(self, textvariable=self.display).pack(side="left", padx=5)
        tk.Label(self, text="(optional)").pack(side="left", padx=5)

    def select_file(self):
        path = tk.filedialog.askopenfilename()
        if path:
            self.path.set(path)
            self.display.set(os.path.basename(path))