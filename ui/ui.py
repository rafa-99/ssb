import tkinter as tk
from .dataset_frame import DatasetFrame
from .executable_frame import ExecutableFrame
from .tree_view import TreeView

from services.ip_utils import collect_ips
from services.firewall import generate_firewall_rules

SIZE = 512

def startUI():
    root = tk.Tk()
    root.title("Firewall Tool")
    root.geometry(f"{SIZE}x{SIZE}")

    data_store = {"data": None}

    top = tk.Frame(root)
    top.pack(anchor="w", pady=5, fill="x")

    tree = TreeView(root)
    dataset = DatasetFrame(
        top,
        on_load=lambda data: load_dataset(tree, data_store, data)
    )
    executable = ExecutableFrame(top)

    dataset.pack(anchor="w", pady=5)
    executable.pack(anchor="w", pady=5)
    tree.pack(fill="both", expand=True, pady=5)
    
    tk.Button(
        root,
        text="Generate Firewall Rules",
        command=lambda: generate_rules_action(tree, executable, data_store)
    ).pack(anchor="w", padx=5, pady=5)

    root.mainloop()

def load_dataset(tree, store, data):
    store["data"] = data
    tree.load_data(data)


def generate_rules_action(tree, executable, store):
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

    print(f"\nGenerated {len(rules)} rule(s):\n")

    for r in rules:
        print(r)

    with open("firewall_rules.ps1", "w") as f:
        f.write("\n".join(rules))

    print("\nSaved to firewall_rules.ps1")