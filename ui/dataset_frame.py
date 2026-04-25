import os
import json
import tkinter as tk
import tkinter.filedialog


class DatasetFrame(tk.Frame):
    def __init__(self, parent, on_load):
        super().__init__(parent)

        self.on_load = on_load
        self.display = tk.StringVar(value="None")

        tk.Button(
            self,
            text="Select Dataset",
            command=self.select_file
        ).pack(side="left", padx=5)

        tk.Label(self, textvariable=self.display).pack(side="left", padx=5)

    def select_file(self):
        path = tk.filedialog.askopenfilename(filetypes=[("JSON", "*.json")])
        if not path:
            return

        self.display.set(os.path.basename(path))

        with open(path) as f:
            data = json.load(f)

        self.on_load(data)