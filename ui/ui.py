import tkinter as tk

from .dataset_frame import DatasetFrame
from .executable_frame import ExecutableFrame
from .tree_view import TreeView

from services.ip_utils import collect_ips
from services.firewall import generate_firewall_rules, apply_rules, remove_rules

SIZE = 512

def startUI():
    root = tk.Tk()
    root.title("Firewall Tool")
    root.geometry(f"{SIZE}x{SIZE}")

    data_store = {"data": None}
    rules_active = {"value": False}

    tree = TreeView(root)
    dataset = DatasetFrame(
        root,
        on_load=lambda data: load_dataset(tree, data_store, data)
    )
    executable = ExecutableFrame(root)

    dataset.pack(anchor="w", pady=5)
    executable.pack(anchor="w", pady=5)
    tree.pack(fill="both", expand=True, pady=5)

    button_text = tk.StringVar(value="Block Servers")

    tk.Button(
        master=root,
        textvariable=button_text,
        command=lambda: toggle_rules(tree, executable, data_store, rules_active, button_text)
    ).pack(anchor="w", padx=5, pady=5)

    root.mainloop()

def load_dataset(tree, store, data):
    store["data"] = data
    tree.load_data(data)

def toggle_rules(tree, executable, store, state, label_var):
    if state["value"]:
        remove_rules()
        label_var.set("Block Servers")
        state["value"] = False
    else:
        apply_rules_ui(tree, executable, store)
        label_var.set("Unblock Servers")
        state["value"] = True


def apply_rules_ui(tree, executable, store):
    data = store["data"]
    exe_path = executable.path.get()

    if not data:
        print("No dataset loaded")
        return

    selected = tree.get_selected()
    ips = collect_ips(data, selected)

    if not ips:
        print("No IPs found")
        return

    rules = generate_firewall_rules(exe_path, ips)

    apply_rules(rules)