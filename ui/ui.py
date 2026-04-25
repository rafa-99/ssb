import tkinter as tk

from .dataset_frame import DatasetFrame
from .executable_frame import ExecutableFrame
from .tree_view import TreeView
from .lower_buttons_frame import LowerButtonsFrame

from utils.resources import resource_path

SIZE = 512

def startUI():
    root = tk.Tk()
    root.title("ssb")
    root.geometry(f"{SIZE}x{SIZE}")
    root.iconbitmap(resource_path("assets/app.ico"))

    data_store = {"data": None, "name": ""}

    tree = TreeView(root)
    dataset = DatasetFrame(
        root,
        on_load=lambda data: load_dataset(tree, data_store, data)
    )
    executable = ExecutableFrame(root)
    lowerButtons = LowerButtonsFrame(root, tree, executable, data_store, {"value": False})

    dataset.pack(anchor="w", pady=5)
    executable.pack(anchor="w", pady=5)
    tree.pack(fill="both", expand=True, pady=5)
    lowerButtons.pack(anchor="w", pady=5)

    root.mainloop()

def load_dataset(tree, store, data):
    store["data"] = data["data"]
    store["name"] = data["name"]
    
    tree.load_data(data["data"])